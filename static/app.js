var table, rows, switching, i, shouldSwitch;
var x = 0, y = 0;

table = document.getElementById("myTable");
switching = true;

// Sorting the Id
while (switching) {
    switching = false;
    rows = table.rows;

    for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;
        x = parseInt(rows[i].getElementsByTagName("TD")[0]);
        y = parseInt(rows[i + 1].getElementsByTagName("TD")[0]); 

        if (x < y) {
        shouldSwitch = true;
        break;
        }
    }

    if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
    }

}
