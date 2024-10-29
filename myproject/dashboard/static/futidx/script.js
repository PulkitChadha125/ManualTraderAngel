// Function to handle buying/selling in the Call panel
document
  .querySelector('.bg-green-100 button:nth-child(1)')
  .addEventListener('click', function () {
    //('Buying order placed')
  })

document
  .querySelector('.bg-green-100 button:nth-child(2)')
  .addEventListener('click', function () {
   // alert('Selling order placed')
  })

// Function to handle buying/selling in the Put panel
document
  .querySelector('.bg-red-100 button:nth-child(1)')
  .addEventListener('click', function () {
  //  alert('Buying order placed')
  })

document
  .querySelector('.bg-red-100 button:nth-child(2)')
  .addEventListener('click', function () {
  //  alert('Selling order placed')
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
 // alert(`${isCall ? 'Call' : 'Put'} strike selected: ${strikeElement.value}`)
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
//done by me
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
///////////
/////////////

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
          //  alert(`Buy FUTIDX pressed\nSymbol: ${symbol}\nExpiry: ${expiry}\nQuantity: ${quantity}`);
        } else {
        //    alert('Please fill out all fields (Symbol, Expiry, and Quantity)');
        }
    });
});



// =============================
// FUTIDX Symbol Handling
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
