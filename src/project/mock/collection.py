from project.models import Collection

dummy_collections = [
    Collection(
        name='Personal collection!',
        description='This is my first collection.',
        user_id=1,
        image_url='http://lorempixel.com/400/200'
    ),
    Collection(
        name='My other collection',
        description='This is my second collection.',
        user_id=1,
        image_url='http://lorempixel.com/400/200'
    ),
    Collection(
        name='Fender Classics',
        description='This is my third collection.',
        user_id=1,
        image_url='http://lorempixel.com/400/200'
    ),
    Collection(
        name='Gibson Classics',
        description='This is my fourth collection.',
        user_id=1,
        image_url='http://lorempixel.com/400/200'
    ),
    Collection(
        name='Test Collection',
        description='This is a test',
        user_id=2
    ),
    Collection(
        name='Gretsch Gods',
        description='This is a collection of Gretsch Guitars',
        user_id=1,
        image_url='http://lorempixel.com/400/200',
        featured=1
    ),
    Collection(
        name='Foo bar baz',
        description='The baz is too much.',
        user_id=1,
        image_url='http://lorempixel.com/400/200',
        featured=1
    ),
    Collection(
        name='Collection sickness',
        description='I am getting sick of adding these',
        user_id=2,
        image_url='http://lorempixel.com/400/200',
        featured=1
    ),
    Collection(
        name='Dunder Miflin',
        description='Michael Scott is a god, Gervais is not.',
        user_id=3,
        image_url='http://lorempixel.com/400/200',
        featured=1
    ),
    Collection(
        name='My last collection',
        description='The last collections that contains some cool stuff',
        user_id=1,
        image_url='http://lorempixel.com/400/200'
    ),
    Collection(
        name='Another collection',
        description='Oh wait there IS another one!',
        user_id=1,
        image_url='http://lorempixel.com/400/200'
    ),
    Collection(
        name='Daniel Moffats collection',
        description='This is my personal collection',
        user_id=1,
        image_url='http://lorempixel.com/400/200'
    )
]
