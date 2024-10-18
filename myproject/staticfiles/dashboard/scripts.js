// =============================
// Dynamic Table Handling
// =============================

// Sample data to simulate fetching from an API
const positionsData = [
  {
    symbol: 'AAPL',
    avgPrice: 150,
    qty: 10,
    sl: 145,
    target: 160,
    pos: 10,
    ltp: 155,
    pnl: 50,
    unrealizedPnL: 25
  },
  {
    symbol: 'GOOGL',
    avgPrice: 2700,
    qty: 5,
    sl: 2650,
    target: 2800,
    pos: 5,
    ltp: 2750,
    pnl: 250,
    unrealizedPnL: 150
  },
  {
    symbol: 'AAPL',
    avgPrice: 150,
    qty: 10,
    sl: 145,
    target: 160,
    pos: 10,
    ltp: 155,
    pnl: 50,
    unrealizedPnL: 25
  },
  {
    symbol: 'GOOGL',
    avgPrice: 2700,
    qty: 5,
    sl: 2650,
    target: 2800,
    pos: 5,
    ltp: 2750,
    pnl: 250,
    unrealizedPnL: 150
  },
  {
    symbol: 'AAPL',
    avgPrice: 150,
    qty: 10,
    sl: 145,
    target: 160,
    pos: 10,
    ltp: 155,
    pnl: 50,
    unrealizedPnL: 25
  },
  {
    symbol: 'GOOGL',
    avgPrice: 2700,
    qty: 5,
    sl: 2650,
    target: 2800,
    pos: 5,
    ltp: 2750,
    pnl: 250,
    unrealizedPnL: 150
  },
  {
    symbol: 'AAPL',
    avgPrice: 150,
    qty: 10,
    sl: 145,
    target: 160,
    pos: 10,
    ltp: 155,
    pnl: 50,
    unrealizedPnL: 25
  },
  {
    symbol: 'GOOGL',
    avgPrice: 2700,
    qty: 5,
    sl: 2650,
    target: 2800,
    pos: 5,
    ltp: 2750,
    pnl: 250,
    unrealizedPnL: 150
  }
]

// Function to load the table with positions data
// function loadPositionsTable(data) {
//     const tbody = document.getElementById('positions-body');
//     tbody.innerHTML = '';  // Clear existing rows

//     data.forEach(position => {
//         const row = document.createElement('tr');
//         row.innerHTML = `
//             <td>${position.symbol}</td>
//             <td>${position.avgPrice}</td>
//             <td>${position.qty}</td>
//             <td>${position.sl}</td>
//             <td>${position.target}</td>
//             <td>${position.pos}</td>
//             <td>${position.ltp}</td>
//             <td>${position.pnl}</td>
//             <td>${position.unrealizedPnL}</td>
//             <td><button class="action-btn" onclick="closePosition('${position.symbol}')">Close</button></td>
//         `;
//         tbody.appendChild(row);
//     });
// }

// // Call this function to initially load the data
// loadPositionsTable(positionsData);

// Function to load table data dynamically
function loadTable (data, type) {
  const tableBody = document.getElementById('positions-body')
  tableBody.innerHTML = '' // Clear the table before loading new data

  let html = ''
  data.forEach(row => {
    html += `<tr>
                        <td>${row.symbol}</td>
                        <td>${row.avgPrice}</td>
                        <td>${row.qty}</td>
                        <td>${row.sl}</td>
                        <td>${row.target}</td>
                        <td>${row.pos}</td>
                        <td>${row.ltp}</td>
                        <td>${row.pl}</td>
                        <td>${row.upl}</td>
                        <td><button class="bg-red-500 text-white px-2 py-1 rounded">Action</button></td>
                    </tr>`
  })

  tableBody.innerHTML = html
}

// Event listeners for the buttons
document.getElementById('positions-tab').addEventListener('click', () => {
  loadTable(positionsData, 'positions')
  highlightTab('positions-tab')
})

document.getElementById('orderbook-tab').addEventListener('click', () => {
  loadTable(positionsData, 'orderbook')
  highlightTab('orderbook-tab')
})

document.getElementById('tradebook-tab').addEventListener('click', () => {
  loadTable(positionsData, 'tradebook')
  highlightTab('tradebook-tab')
})

// Function to highlight the active tab
function highlightTab (activeTabId) {
  const tabs = ['positions-tab', 'orderbook-tab', 'tradebook-tab']
  tabs.forEach(tabId => {
    document.getElementById(tabId).classList.remove('bg-blue-500', 'text-white')
    document.getElementById(tabId).classList.add('bg-gray-300', 'text-black')
  })

  document
    .getElementById(activeTabId)
    .classList.add('bg-blue-500', 'text-white')
  document
    .getElementById(activeTabId)
    .classList.remove('bg-gray-300', 'text-black')
}

// Initially load Positions on page load
window.onload = function () {
  loadTable(positionsData, 'positions')
  highlightTab('positions-tab')
}

// Function to close a position (you can add more functionality here)
function closePosition (symbol) {
  alert(`Closing position for ${symbol}`)
}

// =============================
// Resizable Panel Handling
// =============================

const resizer = document.getElementById('drag-handle')
const leftPanel = document.getElementById('positions-table')
const rightPanel = document.getElementById('order-placement-form')

resizer.addEventListener('mousedown', function (e) {
  document.addEventListener('mousemove', resize)
  document.addEventListener('mouseup', stopResize)
})

function resize (e) {
  const containerWidth = document.getElementById(
    'resizable-container'
  ).offsetWidth
  const newWidth = (e.clientX / containerWidth) * 100
  leftPanel.style.width = newWidth + '%'
  rightPanel.style.width = 100 - newWidth + '%'
}

function stopResize () {
  document.removeEventListener('mousemove', resize)
  document.removeEventListener('mouseup', stopResize)
}

// =============================
// Button Event Handling
// =============================

// Function to handle "Refresh" button click
document
  .getElementById('refresh-button')
  .addEventListener('click', function () {
    alert('Refreshing positions...')
    loadPositionsTable(positionsData) // Simulate a refresh by reloading the table
  })

// Function to handle "Cancel All" button click
document
  .getElementById('cancel-all-button')
  .addEventListener('click', function () {
    alert('Cancelling all orders...')
  })

// Function to handle "Exit All" button click
document
  .getElementById('exit-all-button')
  .addEventListener('click', function () {
    alert('Exiting all positions...')
  })

// =============================
// Order Placement Form Handling
// =============================

// Function to handle buying/selling in the Call panel
document
  .querySelector('.bg-green-100 button:nth-child(1)')
  .addEventListener('click', function () {
    alert('Buying CE order placed')
  })

document
  .querySelector('.bg-green-100 button:nth-child(2)')
  .addEventListener('click', function () {
    alert('Selling CE order placed')
  })

// Function to handle buying/selling in the Put panel
document
  .querySelector('.bg-red-100 button:nth-child(1)')
  .addEventListener('click', function () {
    alert('Buying PE order placed')
  })

document
  .querySelector('.bg-red-100 button:nth-child(2)')
  .addEventListener('click', function () {
    alert('Selling PE order placed')
  })

// Function to handle percentage buttons
function handlePercentageClick (percentage) {
  alert(`${percentage}% selected`)
}

// Add event listeners for percentage buttons
document.querySelectorAll('.grid-cols-4 button').forEach(button => {
  button.addEventListener('click', function () {
    handlePercentageClick(this.textContent)
  })
})

// Function to handle MKT/LTP toggle
function handleMktLtpToggle (isCall) {
  const toggleElement = isCall
    ? document.getElementById('call-mkt-ltp-toggle')
    : document.getElementById('put-mkt-ltp-toggle')
  alert(
    `${isCall ? 'Call' : 'Put'} MKT/LTP toggled: ${
      toggleElement.checked ? 'LTP' : 'MKT'
    }`
  )
}

// Add event listeners for MKT/LTP toggles
document
  .getElementById('call-mkt-ltp-toggle')
  .addEventListener('change', function () {
    handleMktLtpToggle(true)
  })

document
  .getElementById('put-mkt-ltp-toggle')
  .addEventListener('change', function () {
    handleMktLtpToggle(false)
  })

// Function to update LTP values (simulated)
function updateLtpValues () {
  document.getElementById('call-ltp').textContent = (
    Math.random() * 100
  ).toFixed(2)
  document.getElementById('put-ltp').textContent = (
    Math.random() * 100
  ).toFixed(2)
}

// Simulate LTP updates every 5 seconds
setInterval(updateLtpValues, 5000)

// Function to handle strike selection
function handleStrikeSelection (isCall) {
  const strikeElement = isCall
    ? document.getElementById('call-strike')
    : document.getElementById('put-strike')
  alert(`${isCall ? 'Call' : 'Put'} strike selected: ${strikeElement.value}`)
}

// Add event listeners for strike selection
document.getElementById('call-strike').addEventListener('change', function () {
  handleStrikeSelection(true)
})

document.getElementById('put-strike').addEventListener('change', function () {
  handleStrikeSelection(false)
})

// Function to handle limit order placement
function placeLimitOrder (isCall) {
  const priceElement = isCall
    ? document.getElementById('call-limit-price')
    : document.getElementById('put-limit-price')
  const qtyElement = isCall
    ? document.getElementById('call-limit-qty')
    : document.getElementById('put-limit-qty')
  alert(
    `${isCall ? 'Call' : 'Put'} Limit Order: Price ${priceElement.value}, Qty ${
      qtyElement.value
    }`
  )
}

// Add event listeners for limit order buttons
document
  .querySelector('.bg-green-100 button:nth-child(5)')
  .addEventListener('click', function () {
    placeLimitOrder(true)
  })

document
  .querySelector('.bg-red-100 button:nth-child(5)')
  .addEventListener('click', function () {
    placeLimitOrder(false)
  })
