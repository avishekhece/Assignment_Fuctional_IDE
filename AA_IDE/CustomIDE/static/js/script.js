/* Add more styles as needed */

function toggleHistory() {
  var historyContainer = document.getElementById("history-container");
  if (historyContainer.style.display === "block") {
      historyContainer.style.display = "none";
  } else {
      historyContainer.style.display = "block";
  }
}

function showTestCaseDetails(caseNumber) {
  var testCaseDetails = document.getElementById("test-case-details");
  var isVisible = testCaseDetails.style.display === "block";
  
  // If the details are already visible and the same button is clicked again, hide them
  if (isVisible && testCaseDetails.dataset.caseNumber === caseNumber.toString()) {
    testCaseDetails.style.display = "none";
    return;
  }

  // Populate the test case details based on the case number (Replace with actual data)
  var testCaseData = getTestCaseData(caseNumber); // Define this function to get test case data
  testCaseDetails.innerHTML = `
    <h3>Test Case ${caseNumber} Details</h3>
    <p>Input: ${testCaseData.input}</p>
    <p>Target: ${testCaseData.target}</p>
  `;

  // Set the dataset attribute to the clicked case number for comparison
  testCaseDetails.dataset.caseNumber = caseNumber;
  testCaseDetails.style.display = "block";
}

// Function to get test case data (replace with actual data source)
function getTestCaseData(caseNumber) {
  // Example data, replace with actual data retrieval logic
  if (caseNumber === 1) {
      return { input: "[1,2,3]", target: "6" };
  } else if (caseNumber === 2) {
      return { input: "[4,5,6]", target: "12" };
  } else if (caseNumber === 3) {
      return { input: "[7,8,9]", target: "20" };
  }
}

function showAddTestCaseForm() {
  var totalTestCases = document.querySelectorAll('.test-case-button').length;
  var newCaseNumber = totalTestCases + 1;

  var testCaseButton = document.createElement('button');
  testCaseButton.className = 'test-case-button';
  testCaseButton.setAttribute('onclick', `showTestCaseDetails(${newCaseNumber})`);
  testCaseButton.textContent = `Case ${newCaseNumber}`;

  // Append the new button after the existing buttons
  var addButton = document.querySelector('.add-test-case-button');
  addButton.parentNode.insertBefore(testCaseButton, addButton);

  var testCaseDetails = document.getElementById("test-case-details");
  testCaseDetails.innerHTML = `
    <h3>Add Test Case</h3>
    <form onsubmit="return submitTestCase()">
      <label for="input">Input:</label>
      <input type="text" id="input" name="input" required><br>
      <label for="target">Target:</label>
      <input type="text" id="target" name="target" required><br>
      <button type="submit">Submit</button>
    </form>
  `;
}

function submitTestCase() {
  var input = document.getElementById("input").value;
  var target = document.getElementById("target").value;
  // Add code here to process the submitted test case data
  console.log("Submitted Input:", input);
  console.log("Submitted Target:", target);
  return false; // Prevent form submission
}
