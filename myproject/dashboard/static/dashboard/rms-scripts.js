// DOM Elements
const modal = document.getElementById('rmsModal');
const closeButton = document.querySelector('.close-button');
const tabs = document.querySelectorAll('.sidebar li');
const contents = document.querySelectorAll('.tab-content');
const clearButtons = document.querySelectorAll('.clear-btn');
const saveButtons = document.querySelectorAll('.save-btn');
const resetButton = document.querySelector('.reset-btn');
const saveAllButton = document.querySelector('.modal-footer .save-btn');

// Function to open the modal in the current page
function openRMSSettings() {
    modal.style.display = 'block';
}

// Close modal function
function closeModal() {
    modal.style.display = 'none';
}

// Switch tabs function
function switchTab(e) {
    const clickedTab = e.target;
    const targetId = clickedTab.id.replace('-tab', '-content');

    tabs.forEach(tab => tab.classList.remove('active'));
    contents.forEach(content => content.classList.remove('active'));

    clickedTab.classList.add('active');
    document.getElementById(targetId).classList.add('active');
}

// Clear fields function
function clearFields(e) {
    const section = e.target.closest('div');
    const inputs = section.querySelectorAll('input');
    const selects = section.querySelectorAll('select');

    inputs.forEach(input => {
        if (input.type === 'number') {
            input.value = '';
        } else if (input.type === 'radio') {
            input.checked = false;
        }
    });

    selects.forEach(select => {
        select.selectedIndex = 0;
    });
}

// Save settings function (placeholder)
function saveSettings(e) {
    const section = e.target.closest('div');
    console.log('Saving settings for:', section.querySelector('h3').textContent);
    // Here you would typically send the data to a server
    alert('Settings saved successfully!');
}

// Reset all settings function (placeholder)
function resetAllSettings() {
    console.log('Resetting all settings');
    // Here you would typically reset all inputs to default values
    alert('All settings have been reset to default values.');
}

// Save all settings function (placeholder)
function saveAllSettings() {
    console.log('Saving all settings');
    // Here you would typically send all data to a server
    alert('All settings have been saved successfully!');
}

// Event Listeners
closeButton.addEventListener('click', closeModal);
tabs.forEach(tab => tab.addEventListener('click', switchTab));
clearButtons.forEach(button => button.addEventListener('click', clearFields));
saveButtons.forEach(button => button.addEventListener('click', saveSettings));
resetButton.addEventListener('click', resetAllSettings);
saveAllButton.addEventListener('click', saveAllSettings);

// Close modal if clicked outside
window.addEventListener('click', (e) => {
    if (e.target === modal) {
        closeModal();
    }
});

// Expose the openRMSSettings function globally
window.openRMSSettings = openRMSSettings;
