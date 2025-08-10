import os
def test_artifacts():
    os.makedirs('reports', exist_ok=True)
    assert os.path.isdir('reports')
