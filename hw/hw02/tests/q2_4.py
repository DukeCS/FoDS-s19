test = {
  'name': 'Question 2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(pter)
          98
          >>> # It looks like you subtracted in the wrong order.
          >>> round(pter.item(6), 4) != -1.1417
          True
          >>> round(pter.item(6), 4)
          1.1417
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}