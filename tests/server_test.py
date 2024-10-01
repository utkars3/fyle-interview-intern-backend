import json
from core.libs.exceptions import FyleError

# added for improving cov score
def test_ready_route(client):
    response = client.get('/')  # Send a GET request to the root route

    # Check that the response status code is 200
    assert response.status_code == 200

    # Load the response data as JSON
    data = json.loads(response.data)

    # Verify the response structure and content
    assert 'status' in data
    assert data['status'] == 'ready'
    assert 'time' in data




def test_invalid_url(client):
    response = client.get('/invalid-url')  # Send a GET request to a non-existent route

    # Check that the response status code is 404
    assert response.status_code == 404

    # Load the response data as JSON
    data = json.loads(response.data)

    # Verify the response structure and content
    assert 'error' in data
    assert data['error'] == 'NotFound'  # Adjust based on how you handle 404 errors
    assert 'message' in data  # Ensure there's a message indicating what went wrong


def test_fyle_error_to_dict():
    # Create an instance of FyleError
    error = FyleError(status_code=404, message="Not Found")

    # Call the to_dict method
    result = error.to_dict()

    # Assert that the result is as expected
    assert result == {'message': "Not Found"}