The script that considers Total cost by object_type, object_id for all records from files for which there is a user: scalr-meta field of the form

v1 {SCALR_ENV_ID} {SCALR_FARM_ID} {SCALR_FARM_ROLE_ID} {SCALR_SERVER_ID} with non-empty values.

Where object_type is one of four types of resources: env, farm, farm_role, server

And object_id is its value in the scalr-meta tag.

The result is written to the sqlite table.
