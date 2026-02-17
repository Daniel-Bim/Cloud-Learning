# הפעלה כמנהל חובה
if (-not ([bool]([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))) {
    Write-Host "Error: Run PowerShell as Administrator!" -ForegroundColor Red
    break
}

# ספריית התקנה יציבה
$InstallPath = "C:\Program Files\WindowsPowerShell\Modules"

# ודא NuGet מותקן
if (-not (Get-PackageProvider -Name NuGet -ErrorAction SilentlyContinue)) {
    Write-Host "Installing NuGet provider..." -ForegroundColor Yellow
    Install-PackageProvider -Name NuGet -Force -Scope AllUsers
}

# הורד רשימת כל תתי־המודולים של Az מה-PSGallery
Write-Host "Fetching list of Az modules from PSGallery..." -ForegroundColor Cyan
$AllAzModules = Find-Module -Name Az -AllVersions | ForEach-Object {
    (Find-Module -Name $_.Name -Repository PSGallery).Dependencies | ForEach-Object { $_.Name }
} | Sort-Object -Unique
$AllAzModules += "Az"

# התקנת כל מודול בודד
foreach ($mod in $AllAzModules) {
    Write-Host "Installing $mod..." -ForegroundColor Cyan
    Install-Module -Name $mod -Scope AllUsers -Force -Repository PSGallery -Verbose
}

# בדיקה שהמודולים מותקנים
Write-Host "Installed Az modules:" -ForegroundColor Green
Get-Module -ListAvailable | Where-Object { $_.Name -like "Az*" } | Select-Object Name, Version, Path