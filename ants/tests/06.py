test = {
  'name': 'Problem 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '1e8787b3e2ad047f62004362556a5edf',
          'choices': [
            r"""
            instance, each HungryAnt instance digests independently of other
            HungryAnt instances
            """,
            'instance, all HungryAnt instances in the game digest simultaneously',
            r"""
            class, each HungryAnt instance digests independently of other
            HungryAnt instances
            """,
            'class, all HungryAnt instances in the game digest simultaneously'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Should digesting be an instance or class attribute? Why?'
        },
        {
          'answer': '458dbd57c82fe76df45e033d0235d262',
          'choices': [
            'When it is not digesting, i.e. when its digesting attribute is 0',
            'When it is digesting, i.e. when its digesting attribute is at least 1',
            'Each turn',
            'Whenever a Bee is in its place'
          ],
          'hidden': False,
          'locked': True,
          'question': 'When is a HungryAnt able to eat a Bee?'
        },
        {
          'answer': '30589d40710d13dfd27efd5cdd28c0f0',
          'choices': [
            'A random Bee in the same place as itself',
            'The closest Bee in front of it',
            'The closest Bee behind it',
            'The closest Bee in either direction'
          ],
          'hidden': False,
          'locked': True,
          'question': 'When a HungryAnt is able to eat, which Bee does it eat?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing HungryAnt parameters
          >>> hungry = HungryAnt()
          >>> HungryAnt.food_cost
          c9452203eb0b0f0bd2454586a6c2fc5c
          # locked
          >>> hungry.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing HungryAnt eats and digests
          >>> hungry = HungryAnt()
          >>> bee1 = Bee(1000)              # A Bee with 1000 armor
          >>> place = colony.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> place.add_insect(bee1)         # Add the Bee to the same place as HungryAnt
          >>> hungry.action(colony)
          >>> bee1.armor
          73b94a1326ae2e803c3421016112207b
          # locked
          >>> bee2 = Bee(1)                 # A Bee with 1 armor
          >>> place.add_insect(bee2)
          >>> for _ in range(3):
          ...     hungry.action(colony)     # Digesting...not eating
          >>> bee2.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> hungry.action(colony)
          >>> bee2.armor
          73b94a1326ae2e803c3421016112207b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing HungryAnt eats and digests
          >>> hungry = HungryAnt()
          >>> super_bee, wimpy_bee = Bee(1000), Bee(1)
          >>> place = colony.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> place.add_insect(super_bee)
          >>> hungry.action(colony)         # super_bee is no match for HungryAnt!
          >>> super_bee.armor
          0
          >>> place.add_insect(wimpy_bee)
          >>> for _ in range(3):
          ...     hungry.action(colony)     # digesting...not eating
          >>> wimpy_bee.armor
          1
          >>> hungry.action(colony)         # back to eating!
          >>> wimpy_bee.armor
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt only waits when digesting
          >>> hungry = HungryAnt()
          >>> place = colony.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> # Wait a few turns before adding Bee
          >>> for _ in range(5):
          ...     hungry.action(colony)  # shouldn't be digesting
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> hungry.action(colony)  # Eating time!
          >>> bee.armor
          0
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> for _ in range(3):
          ...     hungry.action(colony)     # Should be digesting
          >>> bee.armor
          3
          >>> hungry.action(colony)
          >>> bee.armor
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt digest time looked up on instance
          >>> very_hungry = HungryAnt()  # Add very hungry caterpi- um, ant
          >>> very_hungry.time_to_digest = 0
          >>> place = colony.places["tunnel_0_0"]
          >>> place.add_insect(very_hungry)
          >>> for _ in range(100):
          ...     place.add_insect(Bee(3))
          >>> for _ in range(100):
          ...     very_hungry.action(colony)   # Eat all the bees!
          >>> len(place.bees)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt dies while eating
          >>> hungry = HungryAnt()
          >>> place = colony.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> place.add_insect(Bee(3))
          >>> hungry.action(colony)
          >>> len(place.bees)
          0
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> bee.action(colony) # Bee kills digesting ant
          >>> place.ant is None
          True
          >>> len(place.bees)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt can't eat a bee at another space
          >>> hungry = HungryAnt()
          >>> colony.places["tunnel_0_0"].add_insect(hungry)
          >>> colony.places["tunnel_0_1"].add_insect(Bee(3))
          >>> hungry.action(colony)
          >>> len(colony.places["tunnel_0_1"].bees)
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}