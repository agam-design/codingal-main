// get elements
    const balanceEl = document.getElementById('balance');
    const transactionsEl = document.getElementById('transaction');
    const descriptionEl = document.getElementById('description');
    const amountEl = document.getElementById('amount');
    const typeEl = document.getElementById('type');
    const addBtn = document.getElementById('addtn');

    //transaction array
    let transaction = []

    //load transaction from local storage
window.onload =() =>{
    const savedTransactions= JSON.parse(localStorage.getItem('transaction'));
    if (savedTransactions) {
        transaction= savedTransactions;
        uodateUI();
    }
}
    


