from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
    'deform',
    'googlemaps'
]

setup(name='placebook',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = placebook:main
      """,
)
