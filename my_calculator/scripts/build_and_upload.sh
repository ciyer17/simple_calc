# Exit immediately if a command exits with a non-zero status.
set -e

# Function to display usage information
usage() {
    echo "Usage: $0 {test|prod}"
    echo "  test: Upload to TestPyPI and install from TestPyPI"
    echo "  prod: Upload to PyPI and install from PyPI"
    exit 1
}

cd ..

if [ -d "venv" ]; then
    echo "Virtual environment 'venv' exists. Deleting it..."
    rm -rf venv
fi

python -m venv venv

# Upgrade pip and install required packages
echo "Upgrading pip and installing required packages..."
venv/bin/pip install --upgrade pip
venv/bin/pip install --upgrade setuptools wheel twine

# Clean previous builds
echo "Cleaning up previous builds..."
rm -rf build/ dist/ Chandramouli_Iyer_calculator_0063.egg-info

# Run unit tests
echo "Running unit tests..."
venv/bin/python -m unittest discover tests

# Build the package
echo "Building the package..."
python setup.py sdist bdist_wheel

# Check the distribution files
echo "Checking the distribution files..."
venv/bin/twine check dist/*

# Upload the package
echo "Uploading the package..."
venv/bin/twine upload --verbose --repository-url https://test.pypi.org/legacy/ dist/*

# Install the package
echo "Installing the package..."
venv/bin/pip install --index-url https://test.pypi.org/simple/ Chandramouli-Iyer-calculator-0063

echo "Done!"
