# Get data from http://localhost:5000/calc/5/+10
$response = Invoke-RestMethod -Uri "http://localhost:5000/calc/5/+/10" -Method Get
# check the response and if the result = 15 , then output "Test Passed"
if ($response.result -eq 15) {
    "^_^ Test Passed"
}
else {
    "X_X Test Failed"
}
