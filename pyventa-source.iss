; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{9BE23318-DFC7-4C61-A61C-5E4BF38F26A8}
AppName=Pyventa
AppVersion=2.254
;AppVerName=Pyventa 2.254
AppPublisher=David Osorio
AppPublisherURL=http://www.ottarw.com/pyventa
AppSupportURL=http://www.ottarw.com/pyventa
AppUpdatesURL=http://www.ottarw.com/pyventa
DefaultDirName=/usr/share/pyventa
DisableDirPage=yes
DefaultGroupName=Pyventa
LicenseFile=D:\Documents and Settings\Administrador\Mis documentos\pyventa\admin\Licencia.txt
OutputDir=pyventa-source
OutputBaseFilename=pyventa-2.254
SetupIconFile=D:\usr\share\pyventa_\pyv.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "D:\usr\share\pyventa_\pyventa.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\usr\share\pyventa_\ui_pyventa.pyc"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\usr\share\pyventa_\pyv.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\usr\share\pyventa_\pyventa.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\usr\share\pyventa_\font\*"; DestDir: "{app}\font\"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\usr\share\pyventa_\images\*"; DestDir: "{app}\images\"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\usr\share\pyventa_\import\*"; DestDir: "{app}\import\"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\usr\share\pyventa_\plugins\*"; DestDir: "{app}\plugins\"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\usr\share\pyventa_\sonidos\*"; DestDir: "{app}\sonidos\"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\usr\share\pyventa_\perfil\*"; DestDir: "{app}\perfil\"; Flags:  recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Pyventa"; Filename: "{app}\pyventa.py"
Name: "{commondesktop}\Pyventa"; Filename: "{app}\pyventa.py"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Pyventa"; Filename: "{app}\pyventa.py"; Tasks: quicklaunchicon



