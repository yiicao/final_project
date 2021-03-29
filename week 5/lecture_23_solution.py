import json
import os
import requests


ENDPOINT = 'https://swapi.py4e.com/api' # a global constant

class Crew:
    """Representation of a Starship or Vehicle crew."""

    def __init__(self, members):
        """Initialize Crew instance. Loops over passed in dictionary and calls the built-in
        function setattr() to create an instance variable and assign it a value.

        Parameters:
            members (dict): crew members dictionary (< position >: < Person >)

        Returns:
            None
        """

        for key, val in members.items():
            setattr(self, key, val) # call built-in function

    def __str__(self):
        """Return a string representation of the object."""

        crew = None
        for key, val in self.__dict__.items():
            if crew:
                crew += f", {key}: {val}" # additional member
            else:
                crew = f"{key}: {val}" # 1st member

        return crew

    def remove_by_position(self, positions):
        """Deletes crew position(s) instance variable(s) if name match is obtained from passed in
        postions (e.g., "pilot", "co_pilot", "navigator").

        Parameters:
            positions (list): list of crew positions

        Returns:
            None
        """

        for position in positions:
            if position in self.__dict__.keys():
                delattr(self, position)

    def update(self, members):
        """Adds new instance variables that represent crew postions and assigns crew members from
        passed in members dictionary. Updates existing instance variable values if an instance
        variable is matched by a passed in key (i.e., position).

        Parameters:
            members (dict): members (dict): crew members dictionary (< position >: < Person >)

        Returns:
            None
        """

        for key, val in members.items():
            setattr(self, key, val) # call built-in function


    def jsonable(self):
        """Return a JSON-friendly representation of the object. Loops over instance variables
        and converts person objects to dictionaries.

        Do not simply return self.__dict__. It can be intercepted and mutated, adding, modifying or
        removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        # return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        crew = {}
        for key, val in self.__dict__.items():
            crew[key] = val.jsonable() # person object

        return crew


class Person:
    """Representation of a person.

    Attributes:
        url: uniform resource locator
        name: person name
        birth_year: person's birth_year
        homeworld: person's home planet

    Methods:
        get_homeworld: retrieve home planet
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, birth_year):
        """Initialize a Person instance."""

        self.url = url
        self.name = name
        self.birth_year = birth_year
        self.homeworld = None

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def get_homeworld(self, url):
        """Retrieve SWAPI representation of home planet.
        Convert to Planet instance and assign to person.

        Parameters:
            url (str): resource identifier

        Returns:
            None
        """

        if not self.homeworld:
        # if not isinstance(self.homeworld, Planet):
            data = get_swapi_resource(url)
            self.homeworld = Planet(
                data['url'],
                data['name'],
                data['gravity'],
                data['climate'],
                data['terrain'],
                data['population']
                )

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than built-in dict() to avoid built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and mutated, adding, modifying or
        removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        # return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        return {
                'url': self.url,
                'name': self.name,
                'birth_year': self.birth_year,
                'homeworld': self.homeworld.jsonable()
            }


class Planet:
    """Representation of a planet.

    Attributes:
        url: uniform resource locator
        name: planet name
        gravity: gravity level
        climate: climate description
        terrain: terrain description
        population: population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, gravity, climate, terrain, population):
        """Initialize a Planet instance."""

        self.url = url
        self.name = name
        self.gravity = gravity
        self.climate = climate
        self.terrain = terrain
        self.population = population

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather than
        built-in dict() to avoid built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and mutated, adding, modifying or
        removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        # return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        return {
                'url': self.url,
                'name': self.name,
                'gravity': self.gravity,
                'climate': self.climate,
                'terrain': self.terrain,
                'population': self.population
            }


class Starship:
    """A crewed vehicle used for traveling in realspace or hyperspace.

    Attributes:
        url: uniform resource locator
        name: starship name or nickname
        model: manufacturer's model name
        manufacturer: starship builder
        dimensions: starship length, width, height
        max_atmosphering_speed: max sub-orbital speed
        hyperdrive_rating: lightspeed propulsion system rating
        MGLT: megalight per hour traveled
        crew: crew size
        crew_members: crew (role, name) assigned to starship
        passengers: number of passengers starship rated to carry
        cargo_capacity: cargo metric tonnage starship rated to carry
        consumables: max period in months before on-board provisions must be replenished
        armament: offensive and defensive weaponry

    Methods:
        assign_crew: assign crew members to starship
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.starship_class = None
        self.model = None
        self.manufacturer = None
        self.dimensions = {}
        self.max_atmosphering_speed = None
        self.hyperdrive_rating = None
        self.MGLT = None
        self.armament = []
        self.crew_members = {}
        self.cargo_capacity = None
        self.consumables = None

    def __str__(self):
        """String representation of the object."""

        return f"{self.starship_class} {self.model} {self.name}"


    def assign_crew_members(self, crew):
        """Assign crew_members.

        Parameters:
            crew (Crew): Object comprising crew members (role, person)

        Returns:
            None
        """

        if self.crew_members:
            self.update_crew_members(crew)
        else:
            self.crew_members = crew

    def remove_crew_members_by_position(self, positions):
        """Remove one or more assigned crew_members.

        Parameters:
            position (list): list of positions (instance variable names) to remove

        Returns:
            None
        """

        if self.crew_members:
            self.crew_members.remove_by_position(positions)

    def update_crew_members(self, crew):
        """Update one or more assigned crew_member role(s) and person(s).

        Parameters:
            crew (Crew): Object comprising crew members (role, person)

        Returns:
            None
        """

        if self.crew_members:
            self.crew_members.update(crew)

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather than
        built-in dict() to avoid built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and mutated, adding, modifying or
        removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        # return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        return {
            'url': self.url,
            'name': self.name,
            'starship_class': self.starship_class,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'dimensions': self.dimensions,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'hyperdrive_rating': self.hyperdrive_rating,
            'MGLT': self.MGLT,
            'armament': self.armament,
            'crew_members': self.crew_members.jsonable(), # convert object
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
        }


def get_swapi_resource(url, params=None, timeout=10):
    """Description removed. You will soon write it.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


def read_json(filepath):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict/list: dictionary or list representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        return json.load(file_obj)


def write_json(filepath, data):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict)/(list): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    """Entry point for program. Orchestrates workflow involving
    reading in local data, issuing GET requests to retrieve remote data,
    instantiating class instances, and writing out data as JSON to a file.
    """

    # Debugger-friendly (autograder does not require absolute paths)
    abs_path = os.path.dirname(os.path.abspath(__file__))
    print(f"\n0.0: Absolute directory path = {abs_path}")

    # 1.0 GET/COMBINE MILLENNIUM FALCON DATA

    # 1.1 Retrieve SWAPI representation of the Millennium Falcon (base)
    url = f"{ENDPOINT}/starships"
    params = {'search': 'falcon'}
    swapi_m_falcon = get_swapi_resource(url, params)['results'][0]

    print(f"\n1.1: falcon data = {swapi_m_falcon}\n")


    # 1.2 Read in additional Millenium Falcon data
    filepath = os.path.join(abs_path, 'wookieepedia_m_falcon.json')
    wookiee_m_falcon = read_json(filepath)

    print(f"\n1.2 Wookieepedia M. Falcon data = {wookiee_m_falcon}\n")


    # 1.3 Combine starship data dicts
    # Note: local vals replace swapi vals on matching keys
    swapi_m_falcon.update(wookiee_m_falcon) # in-place (no assignment)

    print(f"\n1.3 M. falcon data (combined) = {swapi_m_falcon}\n")


    # 2.0 WORK WITH CLASS INSTANCES

    # 2.1 Create Starship instance
    m_falcon = Starship(swapi_m_falcon['url'], swapi_m_falcon['name'])
    m_falcon.starship_class = swapi_m_falcon['starship_class']
    m_falcon.model = swapi_m_falcon['model']
    m_falcon.manufacturer = swapi_m_falcon['manufacturer']
    m_falcon.dimensions = swapi_m_falcon['dimensions']
    m_falcon.max_atmosphering_speed = swapi_m_falcon['max_atmosphering_speed']
    m_falcon.hyperdrive_rating = swapi_m_falcon['hyperdrive_rating']
    m_falcon.MGLT = swapi_m_falcon['MGLT']
    m_falcon.armament = swapi_m_falcon['armament']
    m_falcon.cargo_capacity = swapi_m_falcon['cargo_capacity']
    m_falcon.consumables = swapi_m_falcon['consumables']

    print(f"\n2.1: m_falcon.armament = {m_falcon.armament}\n")


    # 3.0 GET CREW MEMBERS
    url = f"{ENDPOINT}/people"


    # 3.1 Get SWAPI Han Solo (Corellian smuggler, pilot)
    params = {'search': 'solo'}
    swapi_solo = get_swapi_resource(url, params)['results'][0]

    print(f"\n3.1: solo data = {swapi_solo}\n")


    # 3.2 Create Person instance/Get Homeworld
    solo = Person(swapi_solo['url'], swapi_solo['name'], swapi_solo['birth_year'])
    solo.get_homeworld(swapi_solo['homeworld'])

    print(f"\n3.2: solo instance = {solo}\n")


    # 3.3 Get SWAPI Chewbacca (Wookiee, co-pilot)
    params = {'search': 'chewbacca'}
    swapi_chewie = get_swapi_resource(url, params)['results'][0]

    print(f"\n3.3: chewie data = {swapi_chewie}\n")


    # 3.4 Create Person instance/Get Homeworld
    chewie = Person(swapi_chewie['url'], swapi_chewie['name'], swapi_chewie['birth_year'])
    chewie.get_homeworld(swapi_chewie['homeworld'])

    print(f"\n3.4: chewie instance = {chewie}\n")


    # 4.0 IMPLEMENT CREW CLASS / INIT, JSONABLE, ASSIGN_CREW METHODS

    crew = Crew({'pilot': solo, 'co-pilot': chewie})

    print(f"\n4.0: Crew = {crew}")

    # 5.0 ASSIGN CREW
    # IMPLEMENT STARSHIP.ASSIGN_CREW() / REVIEW JSONABLE()

    m_falcon.assign_crew_members(crew)

    print(f"\n5.0: Millenium Falcon crew = {crew}")
    print(f"\n5.0: Millenium Falcon crew (jsonable()) = {m_falcon.crew_members.jsonable()}")


    # 6.0 CHANGE PILOT TO REY
    # IMPLEMENT UPDATE_CREW_MEMBERS()

    # 6.1 Get Rey
    params = {'search': 'rey'}
    swapi_rey = get_swapi_resource(url, params)['results'][0]

    print(f"\n6.1: Rey data = {swapi_rey}\n")

    # 6.2 Combine SWAPI (default) and Wookiepedia data
    filepath = os.path.join(abs_path, 'wookieepedia_rey.json')
    fandom_rey = read_json(filepath)
    swapi_rey.update(fandom_rey) # combine

    print(f"\n5.2: Rey data (combined) = {swapi_rey}\n")

    # 6.3 Create Person instance/Get Homeworld
    rey = Person(swapi_rey['url'], swapi_rey['name'], swapi_rey['birth_year'])
    rey.get_homeworld(swapi_rey['homeworld'])

    # 6.4 Swap out Han Solo in favor of Rey
    pilot = {'pilot': rey}
    m_falcon.update_crew_members(pilot)

    print(f"\n5.4: crew = {crew}")
    print(f"\n5.4: Millenium Falcon crew = {m_falcon.crew_members}")


    # 7.0 REMOVE CO-PILOT
    # IMPLEMENT REMOVE_CREW_MEMBERS_BY_POSITION

    m_falcon.remove_crew_members_by_position(['co-pilot'])

    print(f"\n7.0: crew = {crew}")
    print(f"\n7.0: Millenium Falcon crew = {m_falcon.crew_members}")


    # 8.0 WRITE TO FILE

    # 8.1 Reassign Chewbacca as co-pilot (everyone loves Chewie)
    co_pilot = {'co_pilot': chewie}
    m_falcon.update_crew_members(co_pilot)

    print(f"\n8.1: Add Chewie back to crew = {m_falcon.crew_members}")

    # 8.2 Write to file
    filepath = os.path.join(abs_path, 'si506_m_falcon.json')
    write_json(filepath, m_falcon.jsonable())


if __name__ == '__main__':
    main()
