Import-Module ActiveDirectory

$users = Get-Content C:\Script\usuarios.txt

foreach($user in $users)

{

Get-ADUser $user | Set-ADUser -ChangePasswordAtLogon $true

Write-Host "Usuario $user forçado mudar senha no proximo logon"

}
