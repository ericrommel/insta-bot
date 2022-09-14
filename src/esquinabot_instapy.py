from time import sleep

from dotenv import dotenv_values
from instapy import InstaPy
from instapy import smart_run

config = dotenv_values()

# Get an InstaPy session
session = InstaPy(
    username=config.get("USERNAME"),
    password=config.get("PASSWORD"),
    headless_browser=False,  # change it later
    want_check_browser=False,
)

with smart_run(session):
    # General settings
    session.set_relationship_bounds(
        enabled=True,
        delimit_by_numbers=True,
        max_followers=15000,
        min_followers=50,
        min_following=50,
    )

    # Do like some posts that are tagged. List with words in description
    session.like_by_tags(
        tags=[
            "sertao",
            "comida",
            "regional",
            "comidaregional",
            "comidasertaneja",
            "comidasdosertao",
            "delicias",
        ],
        amount=5
    )

    # ToDo: Set it later. A subscription is needed: https://www.clarifai.com/
    # session.set_use_clarifai(
    #     enabled=True,
    #     api_key='<your_api_key>'
    # )
    # session.clarifai_check_img_for(
    #     ['nsfw']
    # )

    # Don’t like inappropriate posts. List with inappropriate words in description
    session.set_dont_like(
        tags=[
            "naked",
            "nsfw",
        ]
    )

    # Follow some of authors of the posts
    session.set_do_follow(enabled=True, percentage=50)

    # Write a comment in some posts
    session.set_do_comment(True, percentage=50)
    session.set_comments(
        comments=[
            "Delícia",
            "Eu quero",
            "Lindo :heart_eyes:"
        ]
    )

    # Avoid to be banned setting a quota supervisor
    session.set_quota_supervisor(
        enabled=True,
        peak_comments_daily=240,
        peak_comments_hourly=21
    )
