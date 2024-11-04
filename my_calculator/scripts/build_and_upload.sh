# Exit immediately if a command exits with a non-zero status.
set -e

# Function to display usage information
usage() {
    echo "Usage: $0 {test|prod}"
    echo "  test: Upload to TestPyPI and install from TestPyPI"
    echo "  prod: Upload to PyPI and install from PyPI"
    exit 1
}

# Upgrade pip and install required packages
echo "Upgrading pip and installing required packages..."
pip install --upgrade pip
pip install --upgrade setuptools wheel twine

# Clean previous builds
echo "Cleaning up previous builds..."
rm -rf build/ dist/ my_calculator.egg-info/

# Run unit tests
echo "Running unit tests..."
python -m unittest discover tests

# Build the package
echo "Building the package..."
python setup.py sdist bdist_wheel

# Check the distribution files
echo "Checking the distribution files..."
twine check dist/*

# Upload the package
echo "Uploading the package..."
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Install the package
echo "Installing the package..."
pip install --index-url https://test.pypi.org/simple/ Chandramouli-Iyer-calculator-0063

# Deactivate virtual environment
deactivate

echo "Done!"
