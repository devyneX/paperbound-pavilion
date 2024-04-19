from src.accounts.models import Address, User


def make_fake_user(fake, **kwargs):
    user = User(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        username=fake.user_name(),
        password=fake.password(),
        phone=fake.random_number(digits=20)
    )

    for key, value in kwargs.items():
        setattr(user, key, value)

    user.save()

    return user


def make_fake_address(fake, user, **kwargs):
    address = Address(
        house=fake.building_number(),
        street=fake.street_name(),
        city=fake.city(),
        state=fake.state(),
        country=fake.country_code(),
        post_code=fake.postcode(),
        user=user
    )

    for key, value in kwargs.items():
        setattr(address, key, value)

    address.save()

    return address
