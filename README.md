# JIRA MIGRATE DASHBOARDS WITH 'CUSTOM CHARTS' GADGETS FROM DATA CENTER TO CLOUD

This script is designed to migrate dashboards with the 'custom charts' plugin from Jira Data Center to Jira Cloud.

## How it works

1. **Entering Dashboard Information**: First, you need to enter the basic dashboard information and configuration from Data Center.

2. **Batch Processing**: The script retrieves all dashboards to check if the dashboard and gadget exist on the cloud.

3. **Updating Dashboard Gadget**: If the dashboard and gadget exist on the cloud, the gadget will be updated. If they don't exist, the script will first create a new dashboard and gadget and then update that new gadget with the given configuration.

## Usage

### Prerequisites
Before running the script, ensure you have the following:

- A compatible version of Jira Data Center.
- Required libraries or packages installed (provide details).
- Proper authentication credentials (if needed).

### Example
To use this script, follow these steps:

1. Provide the following dashboard information:
   - Dashboard name
   - Edit permission
   - Share permission
   - Project ID
   - Gadget name
   - Gadget configuration (exported from Data Center)

2. Run the script


### Security and Authentication
Ensure that your authentication credentials are kept secure. Do not include sensitive information directly in the script or in publicly accessible files.
