// Get elements
const balanceEl = document.getElementById('balance');
const transactionsEl = document.getElementById('transactions');
const descriptionEl = document.getElementById('description');
const amountEl = document.getElementById('amount');
const typeEl = document.getElementById('type');
const addBtn = document.getElementById('addBtn');

// Transactions array
let transactions = [];

// Load transactions from localStorage
window.onload = () => {
    const savedTransactions = JSON.parse(localStorage.getItem('transactions'));
    if (savedTransactions) {
        transactions = savedTransactions;
        updateUI();
    }
};

// Function to format numbers in Indian Rupees
function formatINR(amount) {
    return new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(amount);
}

// Add transaction
addBtn.addEventListener('click', () => {
    const description = descriptionEl.value.trim();
    const amount = parseFloat(amountEl.value);
    const type = typeEl.value;

    if (description === '' || isNaN(amount)) {
        alert('Please enter valid description and amount.');
        return;
    }

    const transaction = { description, amount, type };
    transactions.push(transaction);
    updateUI();

    // Clear inputs
    descriptionEl.value = '';
    amountEl.value = '';
});

// Update UI
function updateUI() {
    // Clear transactions list
    transactionsEl.innerHTML = '';

    // Display transactions
    transactions.forEach((tx, index) => {
        const li = document.createElement('li');
        li.textContent = `${tx.description}: ${formatINR(tx.amount)}`;
        li.classList.add(tx.type);

        // Optional: delete button
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.classList.add('delete-btn');
        deleteBtn.addEventListener('click', () => {
            transactions.splice(index, 1);
            updateUI();
        });

        li.appendChild(deleteBtn);
        transactionsEl.appendChild(li);
    });

    // Calculate balance
    const balance = transactions.reduce((acc, tx) => {
        return tx.type === 'income' ? acc + tx.amount : acc - tx.amount;
    }, 0);

    // Display balance in INR
    balanceEl.textContent = formatINR(balance);

    // Save transactions to localStorage
    localStorage.setItem('transactions', JSON.stringify(transactions));
}
