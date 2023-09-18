# Import AWS Tools for PowerShell module
Import-Module AWSPowerShell

# AWS Lambda function name
$lambdaFunctionAddEquipment = 'HealthEquipLambdaAddEquipment'
$lambdaFunctionUpdateEquipment = 'HealthEquipLambdaUpdateEquipment'
$lambdaFunctionGetEquipment = 'HealthEquipLambdaGetEquipment'

# Menu for user selection
$menu = @"
Select an option:
1. Add Equipment
2. Update Equipment
3. Get Equipment
4. Quit
"@

# Loop for user input
do {
    Write-Host $menu
    $choice = Read-Host "Enter your choice: "

    switch ($choice) {
        '1' {
            $name = Read-Host "Enter equipment name: "
            $description = Read-Host "Enter equipment description: "
            $statusId = Read-Host "Enter status ID (1 or 2): "
            $locationId = Read-Host "Enter location ID (1 or 2): "
            # Invoke Lambda function for Option 1: Add Equipment
            $result = Invoke-LMFunction -FunctionName $lambdaFunctionAddEquipment -Payload '{"equipment": {"name": $name, "description": $description, "statusId": $statusId, "locationId": $locationId}}'
            Write-Host "Result: $result"
        }
        '2' {
            $equipId = Read-Host "Enter equipment ID: "
            $statusId = Read-Host "Enter new status ID (1 or 2): "
            # Invoke Lambda function for Option 2: Update Equipment
            $result = Invoke-LMFunction -FunctionName $lambdaFunctionUpdateEquipment -Payload '{"equipId": $equipId, "statusId": $statusId}'
            Write-Host "Result: $result"
        }
        '3' {
            $equipId = Read-Host "Enter equipment ID: "
            # Invoke Lambda function for Option 3: Get Equipment
            $result = Invoke-LMFunction -FunctionName $lambdaFunctionGetEquipment -Payload '{"equipId": ${equipId}}'
            Write-Host "Result: $result"
        }
        '4' {
            # Exit the script
            Write-Host "Exiting..."
            exit
        }
        default {
            Write-Host "Invalid choice. Please select a valid option."
        }
    }
} while ($true)
