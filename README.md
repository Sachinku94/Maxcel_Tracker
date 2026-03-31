
## 📚 Testing Framework Overview

### What is Maxcel Tracker?

Maxcel Tracker is a comprehensive Selenium-based test automation framework built with Python that specializes in web application UI testing and functionality validation. It automates manual testing tasks such as clicking elements, verifying page redirections, checking for broken links, and validating page functionality across different browsers and environments.

### Key Features

#### 1. **Web UI Automation**
- Automate user interactions like clicks, form fills, and navigation
- Test element visibility, enabled/disabled states
- Validate dynamic content loading
- Handle dropdown selections and multi-select operations
- Test drag-and-drop functionality

#### 2. **Functionality Testing**
- Verify button clicks and their outcomes
- Validate form submissions and data entry
- Test page transitions and redirections
- Confirm error message displays
- Validate success confirmations

#### 3. **Link & Navigation Testing**
- Detect broken links on web pages
- Verify correct page redirections
- Test navigation menu functionality
- Validate breadcrumb navigation
- Check page load status codes

#### 4. **Page Validation**
- Verify page elements are loaded correctly
- Validate text content and labels
- Check element positioning and visibility
- Verify images are loaded properly
- Validate page titles and meta information

#### 5. **Cross-Browser Testing**
- Test on Chrome, Firefox, Safari, Edge browsers
- Handle browser-specific issues
- Verify responsive design layouts
- Test on different screen resolutions

#### 6. **Advanced Reporting**
- Beautiful Allure HTML reports with screenshots
- Test execution history and trends
- Failure screenshots for debugging
- Detailed logs for each test step
- Video recording of test execution (optional)

### What Gets Tested

✅ **Element Interactions**
- Clicking buttons, links, and elements
- Entering text in input fields
- Selecting dropdown options
- Checking/unchecking checkboxes
- Hovering over elements

✅ **Page Navigation**
- Page redirection verification
- Back/forward button functionality
- Link navigation testing
- Menu navigation flows
- URL validation

✅ **Broken Links & Pages**
- Identify dead links (404 errors)
- Check external link accessibility
- Validate link targets
- Verify all page elements load
- Check for 500 server errors

✅ **Functionality Validation**
- Form submission and validation
- Error message displays
- Success message confirmations
- Page state changes after actions
- Data persistence and updates

✅ **Page Content**
- Text content verification
- Image loading and display
- Page title and heading validation
- Label and placeholder text
- Dynamic content updates

## 🔧 Prerequisite & How to Run

### Prerequisites

#### System Requirements
- **Python**: 3.8 or higher
- **pip**: Python package manager (comes with Python)
- **Java**: JDK 8 or higher (required for Allure Report)
- **Node.js**: npm (for Allure CLI tool)
- **Git**: For cloning the repository

#### Verify Prerequisites Installation

```bash
# Check Python version
python --version

# Check pip version
pip --version

# Check Java version (required for Allure)
java -version

# Check Node.js/npm version
npm --version

- Install all dependencies create your own venv through requirement.txt to install dependencies
- use Python -m pytest -k testname
- Install allure reporting tool in your system
- Use --alluredir=allure-results
- allure serve allure-results 































