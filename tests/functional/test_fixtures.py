import json

from app import create_app


def test_get_fixtures():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/jsonapi/fixtures' is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/jsonapi/fixtures')
        assert response.status_code == 200


def test_create_fixture_with_new_data():
    # todo not complete
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        example_fixture_payload = {
            'homeTeamName': 'homeTeamName',
            'awayTeamName': 'awayTeamName',
            'fixtureDate': '31/08/2013',
            'FTHG': 1,
            'FTAG': 1,
        }
        response = test_client.post('/main/season/1/league/1/create_fixtures', data=json.dumps(example_fixture_payload))
        assert response.status_code == 201

