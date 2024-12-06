let salesChart;
const year_selector = document.querySelector('#year-selector')
const total_sale = document.querySelector('#total_sale')
const total_orders = document.querySelector('#total_orders')

async function dashboard_info() {
    const ctx = document.getElementById('salesChart').getContext('2d');

    // Destroy existing chart if it exists
    if (salesChart) {
        salesChart.destroy();
    }

    const response = await fetch('/api/transaction/dashboard', {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'year': year_selector.value })
    });

    const response_json = await response.json();

    total_sale.textContent = `₱${response_json.total_price}`
    total_orders.textContent = response_json.total_orders
    // Sales data
    const salesData = {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Sales',
            data: response_json.sales_per_month,
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    };

    // Chart configuration
    const config = {
        type: 'line',
        data: salesData,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Monthly Sales Trend'
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function (value) {
                            return '$' + value.toLocaleString();
                        }
                    }
                }
            }
        }
    };

    // Create the chart and assign it to `salesChart`
    salesChart = new Chart(ctx, config);
}


dashboard_info()