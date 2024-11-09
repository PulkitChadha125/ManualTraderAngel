// =============================
// Dynamic Table Handling
// =============================

// Sample data to simulate fetching from an API
//const positionsData = [
//  {
//    symbol: 'AAPL',
//    avgPrice: 150,
//    qty: 10,
//    sl: 145,
//    target: 160,
//    pos: 10,
//    ltp: 155,
//    pnl: 50,
//    unrealizedPnL: 25
//  },
//  {
//    symbol: 'GOOGL',
//    avgPrice: 2700,
//    qty: 5,
//    sl: 2650,
//    target: 2800,
//    pos: 5,
//    ltp: 2750,
//    pnl: 250,
//    unrealizedPnL: 150
//  },
//  {
//    symbol: 'AAPL',
//    avgPrice: 150,
//    qty: 10,
//    sl: 145,
//    target: 160,
//    pos: 10,
//    ltp: 155,
//    pnl: 50,
//    unrealizedPnL: 25
//  },
//  {
//    symbol: 'GOOGL',
//    avgPrice: 2700,
//    qty: 5,
//    sl: 2650,
//    target: 2800,
//    pos: 5,
//    ltp: 2750,
//    pnl: 250,
//    unrealizedPnL: 150
//  },
//  {
//    symbol: 'AAPL',
//    avgPrice: 150,
//    qty: 10,
//    sl: 145,
//    target: 160,
//    pos: 10,
//    ltp: 155,
//    pnl: 50,
//    unrealizedPnL: 25
//  },
//  {
//    symbol: 'GOOGL',
//    avgPrice: 2700,
//    qty: 5,
//    sl: 2650,
//    target: 2800,
//    pos: 5,
//    ltp: 2750,
//    pnl: 250,
//    unrealizedPnL: 150
//  },
//  {
//    symbol: 'AAPL',
//    avgPrice: 150,
//    qty: 10,
//    sl: 145,
//    target: 160,
//    pos: 10,
//    ltp: 155,
//    pnl: 50,
//    unrealizedPnL: 25
//  },
//  {
//    symbol: 'GOOGL',
//    avgPrice: 2700,
//    qty: 5,
//    sl: 2650,
//    target: 2800,
//    pos: 5,
//    ltp: 2750,
//    pnl: 250,
//    unrealizedPnL: 150
//  }
//]


//function loadTable (data, type) {
//  const tableBody = document.getElementById('positions-body')
//  tableBody.innerHTML = '' // Clear the table before loading new data
//
//  let html = ''
//  data.forEach(row => {
//    html += `<tr>
//                        <td>${row.symbol}</td>
//                        <td>${row.avgPrice}</td>
//                        <td>${row.qty}</td>
//                        <td>${row.sl}</td>
//                        <td>${row.target}</td>
//                        <td>${row.pos}</td>
//                        <td>${row.ltp}</td>
//                        <td>${row.pl}</td>
//                        <td>${row.upl}</td>
//                        <td><button class="bg-red-500 text-white px-2 py-1 rounded">Action</button></td>
//                    </tr>`
//  })
//
//  tableBody.innerHTML = html
//}

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
 // alert(`Closing position for ${symbol}`)
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
 //   alert('Refreshing positions...')
    loadPositionsTable(positionsData) // Simulate a refresh by reloading the table
  })

// Function to handle "Cancel All" button click
document
  .getElementById('cancel-all-button')
  .addEventListener('click', function () {
   // alert('Cancelling all orders...')
  })

// Function to handle "Exit All" button click
document
  .getElementById('exit-all-button')
  .addEventListener('click', function () {
  //  alert('Exiting all positions...')
  })

// =============================
// Order Placement Form Handling
// =============================

// Function to handle buying/selling in the Call panel
document
  .querySelector('.bg-green-100 button:nth-child(1)')
  .addEventListener('click', function () {
 //   alert('Buying CE order placed')
  })

document
  .querySelector('.bg-green-100 button:nth-child(2)')
  .addEventListener('click', function () {
 //   alert('Selling CE order placed')
  })

// Function to handle buying/selling in the Put panel
document
  .querySelector('.bg-red-100 button:nth-child(1)')
  .addEventListener('click', function () {
  //  alert('Buying PE order placed')
  })

document
  .querySelector('.bg-red-100 button:nth-child(2)')
  .addEventListener('click', function () {
 //   alert('Selling PE order placed')
  })

// Function to handle percentage buttons
function handlePercentageClick (percentage) {
 // alert(`${percentage}% selected`)
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
//  alert(
//    `${isCall ? 'Call' : 'Put'} MKT/LTP toggled: ${
//      toggleElement.checked ? 'LTP' : 'MKT'
//    }`
//  )
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
//function updateLtpValues () {
//  document.getElementById('call-ltp').textContent = (
//    Math.random() * 100
//  ).toFixed(2)
//  document.getElementById('put-ltp').textContent = (
//    Math.random() * 100
//  ).toFixed(2)
//}

// Simulate LTP updates every 5 seconds
setInterval(updateLtpValues, 5000)

// Function to handle strike selection
function handleStrikeSelection (isCall) {
  const strikeElement = isCall
    ? document.getElementById('call-strike')
    : document.getElementById('put-strike')
//  alert(`${isCall ? 'Call' : 'Put'} strike selected: ${strikeElement.value}`)
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
//  alert(
//    `${isCall ? 'Call' : 'Put'} Limit Order: Price ${priceElement.value}, Qty ${
//      qtyElement.value
//    }`
//  )
}

// Add event listeners for limit order buttons
document.addEventListener("DOMContentLoaded", function() {
  // Make sure the element exists before attaching the event listener
  var button = document.querySelector('.bg-green-100 button:nth-child(5)');

  // Check if the button exists before adding the event listener
  if (button) {
    button.addEventListener('click', function() {
      // Call the placeLimitOrder function when the button is clicked
      placeLimitOrder(true);
    });
  } else {
    console.error('Button not found!');
  }
});


document
  .querySelector('.bg-red-100 button:nth-child(5)')
  .addEventListener('click', function () {
    placeLimitOrder(false)
  })


  /// edit done by me


  function showOptidx() {
    // Show OPTIDX panel and hide FUTIDX panel
    document.getElementById('optidx-panel').classList.remove('hidden');
    document.getElementById('futidx-panel').classList.add('hidden');

    // Activate OPTIDX button, deactivate FUTIDX button
    document.getElementById('optidx-btn').classList.add('active');
    document.getElementById('futidx-btn').classList.remove('active');
}

function showFutidx() {
    // Show FUTIDX panel and hide OPTIDX panel
    document.getElementById('futidx-panel').classList.remove('hidden');
    document.getElementById('optidx-panel').classList.add('hidden');

    // Activate FUTIDX button, deactivate OPTIDX button
    document.getElementById('futidx-btn').classList.add('active');
    document.getElementById('optidx-btn').classList.remove('active');
}


//////////////////// event to handle button click in futidx buy
document.addEventListener("DOMContentLoaded", function () {
    // Add event listener for the FUTIDX BUY button
    document.getElementById('futidx-buy-btn').addEventListener('click', function () {
        // Get the selected values
        const symbol = document.getElementById('futidx-symbol').value;
        const expiry = document.getElementById('futidx-expiry').value;
        const quantity = document.getElementById('futidx-quantity').value;

        // Check if the required fields are filled
        if (symbol && expiry && quantity) {
            // Display the values in an alert (for now)
           // alert(`Buy FUTIDX pressed\nSymbol: ${symbol}\nExpiry: ${expiry}\nQuantity: ${quantity}`);
        } else {
          //  alert('Please fill out all fields (Symbol, Expiry, and Quantity)');
        }
    });
});









/////////////
// =============================
// Dynamic FUTIDX Event Listener
// =============================
document.getElementById('futidx-symbol').addEventListener('change', function () {
    const symbol = this.value;
    const expirySelect = document.getElementById('futidx-expiry');
    const lotSizeSelect = document.getElementById('futidx-lot-size');
    const quantityInput = document.getElementById('futidx-quantity');

    expirySelect.innerHTML = '<option value="">Select Expiry</option>';
    lotSizeSelect.innerHTML = '<option value="">Select Lots</option>';

    const currentDate = new Date();
    let expiryDate;

    if (symbol === 'NIFTY' || symbol === 'BANKNIFTY') {
        expiryDate = getLastThursday(currentDate);
    } else if (symbol === 'MIDCAPNIFTY') {
        expiryDate = getLastMonday(currentDate);
    } else if (symbol === 'FINNIFTY') {
        expiryDate = getLastTuesday(currentDate);
    }

    if (expiryDate) {
        const option = document.createElement('option');
        option.value = expiryDate.toISOString().split('T')[0];
        option.text = expiryDate.toDateString();
        expirySelect.appendChild(option);
    }

    let lotSizeMultiplier;
    if (symbol === 'NIFTY' || symbol === 'FINNIFTY') {
        lotSizeMultiplier = 25;
    } else if (symbol === 'BANKNIFTY') {
        lotSizeMultiplier = 15;
    } else if (symbol === 'MIDCAPNIFTY') {
        lotSizeMultiplier = 50;
    }

    for (let i = lotSizeMultiplier; i <= 5000; i += lotSizeMultiplier) {
        const option = document.createElement('option');
        option.value = i;
        option.text = i;
        lotSizeSelect.appendChild(option);
    }

    lotSizeSelect.addEventListener('change', function () {
        quantityInput.value = this.value;
    });

    quantityInput.addEventListener('input', function () {
        const lots = parseInt(this.value);
        if (lots % lotSizeMultiplier === 0 && lots <= 5000) {
            lotSizeSelect.value = lots;
        } else {
            lotSizeSelect.value = '';
        }
    });
});

// Function to get the last Thursday of the month (for NIFTY and BANKNIFTY)
function getLastThursday(date) {
    const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
    const dayOfWeek = lastDay.getDay();
    const offset = (dayOfWeek >= 4) ? dayOfWeek - 4 : 7 - (4 - dayOfWeek);
    lastDay.setDate(lastDay.getDate() - offset);
    return lastDay;
}

// Add event listeners for MKT/LTP toggles
document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM fully loaded");

    var callMktToggle = document.getElementById('call-mkt-ltp-toggle');
    var putMktToggle = document.getElementById('put-mkt-ltp-toggle');

    if (callMktToggle) {
        console.log("Call MKT/LTP Toggle exists");
        callMktToggle.addEventListener('change', function () {
            handleMktLtpToggle(true);
        });
    } else {
        console.log("Call MKT/LTP Toggle not found");
    }

    if (putMktToggle) {
        console.log("Put MKT/LTP Toggle exists");
        putMktToggle.addEventListener('change', function () {
            handleMktLtpToggle(false);
        });
    } else {
        console.log("Put MKT/LTP Toggle not found");
    }
});

// MKT/LTP Toggle Handling Function
function handleMktLtpToggle(isCall) {
    const toggleElement = isCall ? document.getElementById('call-mkt-ltp-toggle') : document.getElementById('put-mkt-ltp-toggle');
  //  alert(`${isCall ? 'Call' : 'Put'} MKT/LTP toggled: ${toggleElement.checked ? 'LTP' : 'MKT'}`);
}
