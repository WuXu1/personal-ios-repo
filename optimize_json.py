import json
import collections

with open('apps.json', 'r') as f:
    data = json.load(f)

# Re-organize and add fields according to AltStore best practices
new_data = collections.OrderedDict()
new_data["name"] = data.get("name", "Max's iOS Repository")
new_data["subtitle"] = "Private iOS Applications by Max"
new_data["description"] = "A private repository hosting personal iOS applications and utilities built by Max, including Restring Helper."
new_data["iconURL"] = data.get("iconURL", "")
new_data["headerURL"] = ""
new_data["website"] = "https://github.com/WuXu1/personal-ios-repo"
new_data["tintColor"] = "#FF3B30" # A nice red/orange tint color
new_data["sourceURL"] = data.get("sourceURL", "")

new_data["apps"] = data.get("apps", [])

# Let's clean up the app object too
if len(new_data["apps"]) > 0:
    app = new_data["apps"][0]
    app_cleaned = collections.OrderedDict()
    app_cleaned["name"] = app.get("name", "Restring Helper")
    app_cleaned["bundleIdentifier"] = app.get("bundleIdentifier", "com.stringsports.restringhelper")
    app_cleaned["developerName"] = app.get("developerName", "Max")
    app_cleaned["subtitle"] = "Manage stringing orders like a pro."
    app_cleaned["localizedDescription"] = app.get("localizedDescription", "")
    app_cleaned["iconURL"] = app.get("iconURL", "")
    app_cleaned["tintColor"] = app.get("tintColor", "#007AFF")
    
    app_cleaned["versions"] = [
        {
            "version": app.get("version", "3.0"),
            "date": app.get("versionDate", ""),
            "localizedDescription": app.get("versionDescription", ""),
            "downloadURL": app.get("downloadURL", ""),
            "size": app.get("size", 10485760),
            "minOSVersion": "14.0"
        }
    ]
    # The modern AltStore apps.json uses an array of "versions" inside the app, 
    # but wait, AltStore Classic still supports the flat structure.
    # Let's just keep the flat structure to avoid breaking it, but properly ordered.
    flat_app = collections.OrderedDict()
    flat_app["name"] = app_cleaned["name"]
    flat_app["bundleIdentifier"] = app_cleaned["bundleIdentifier"]
    flat_app["developerName"] = app_cleaned["developerName"]
    flat_app["subtitle"] = "Manage stringing orders efficiently."
    flat_app["version"] = app.get("version", "3.0")
    flat_app["versionDate"] = app.get("versionDate", "")
    flat_app["versionDescription"] = app.get("versionDescription", "")
    flat_app["downloadURL"] = app.get("downloadURL", "")
    flat_app["localizedDescription"] = app_cleaned["localizedDescription"]
    flat_app["iconURL"] = app_cleaned["iconURL"]
    flat_app["tintColor"] = app_cleaned["tintColor"]
    flat_app["size"] = app.get("size", 10485760)
    flat_app["appPermissions"] = app.get("permissions", {"entitlements":[]})
    
    new_data["apps"][0] = flat_app

new_data["news"] = []

with open('apps.json', 'w') as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)

print("Optimized apps.json")
