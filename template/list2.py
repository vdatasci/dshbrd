<head>
<style>
table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    text-align: left;
    padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
    background-color: #3498DB;
    color: white;
}

.panel-success > .panel-footer {
    color: #468847;
    background-color: #dff0d8;
    border-color: #d6e9c6;
}
.panel-heading > .table, .panel-heading > .table th {
    margin:0px;
    border: 0px;
}


</style>
</head>


{{ df2|safe }}
