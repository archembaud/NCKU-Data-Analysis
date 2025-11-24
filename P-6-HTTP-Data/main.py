import pandas as pd
import requests

# This is the URL holding the data we wish to process
GGK_URL="https://ggk-stack-test.ggk.archembaud.com"

def get_rules_for_user(user_id):
    header = {
        "Authorization": f"{user_id}"
    }
    response = requests.get(f"{GGK_URL}/rules", headers=header)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get rules for user {user_id}: {response.status_code}")
        return None


if __name__ == "__main__":
    # Fetch data for these users
    users = [
        "29c4f681-4baa-4f68-83af-120a5ec1210c",
        "c9544cb4-0064-49b2-8ee8-6a8e2706bcaf",
        "75adfe1d-2f27-4f4c-9cf4-c17ed2fdc4fe",
        "01a16664-05bb-4585-a0b2-96d4e2835c7c",
        "c0fe91a7-cfc9-4527-967b-4b9b9e1ed730",
        "84e35798-790c-4a2f-ad95-1644e0d07c60",
        "e0ca46d4-d159-4f20-ac8b-9dcd03c024c0"
    ]
    # Create an empty dataframe
    rules_df = pd.DataFrame()
    for user_id in users:
        user_rules = get_rules_for_user(user_id)
        print(f"Fetched {len(user_rules['rules'])} for user {user_id} from the server")
        # Now to add each rule to the rules dataframe
        for rule in user_rules['rules']:
            rule_record = {
                "user_id": user_id,
                "date_created": rule['dateCreated'],
                "date_modified": rule['dateModified'],
                "rule_id": rule['ruleId'],
                "rule_api": rule['ruleAPI'],
                "userRules": str(rule['userRules'])
            }
            rules_df = pd.concat([rules_df, pd.DataFrame([rule_record])], ignore_index=True)

    # Print out the combined dataframe, and save it to CSV
    print("Combined Rules DataFrame:")
    print(rules_df)
    rules_df.to_csv('combined_rules_data.csv', index=False)

    # Check for the number of rules for each user in the dataframe
    # This should be in agreement with what was fetched from the server above
    for user_id in users:
        user_rule_count = rules_df[rules_df['user_id'] == user_id].shape[0]
        print(f"User {user_id} has {user_rule_count} rules in the combined dataframe.")