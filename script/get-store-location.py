"""Get McDonald's store locations in Japan"""
import json
import os
import requests

def main():
    """Get McDonald's store locations ing page to get the total number of active users."""
    API_URL = "https://map.mcdonalds.co.jp/api/poi"
    STORE_LOCATION_FILENAME = "store-location.json"

    orig_res = requests.get(API_URL)
    orig_res_json = json.loads(orig_res.text)

    necessary_store_info = []
    necessary_store_fields = ("name", "latitude", "longitude", "address")
    for orig_store in orig_res_json:
        store = {"id": ""} # Add the default ID so that `id` comes first in JSON
        for field in necessary_store_fields:
            if field not in orig_store:
                # TODO(k1832): Add an error log
                break

            store[field] = orig_store[field]
        else:
            # The original data contains `id` too, however, it could change
            # over time. So use this format to maintain the compatibility.
            store["id"] = f"{store['latitude']}+{store['longitude']}"
            necessary_store_info.append(store)

    print(f"Original length: {len(orig_res_json)}")
    print(f"After cleaning: {len(necessary_store_info)}")

    # GitHub Pages does not allow to specify the directory to deploy
    # except the "docs" directory
    # (root)
    #   - script
    #       - {this Python script}
    #   - docs
    #       - api
    #           - v1
    #               - {JSON file}
    script_dir_path = os.path.abspath(os.path.dirname(__file__))
    root_dir_path = os.path.dirname(script_dir_path)
    docs_dir_path = os.path.join(root_dir_path, "docs")
    api_dir_path = os.path.join(docs_dir_path, "api")
    api_v1_dir_path = os.path.join(api_dir_path, "v1")

    with open(os.path.join(api_v1_dir_path, STORE_LOCATION_FILENAME), 'w', encoding='utf-8') as f:
        f.write(json.dumps(necessary_store_info, ensure_ascii=False))

if __name__ == "__main__":
    main()
