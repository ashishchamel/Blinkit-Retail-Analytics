{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5161341-d9b0-4c01-b5a4-9c74326da385",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load raw data\n",
    "\n",
    "df = pd.read_csv(r\"C:\\Users\\007bo\\OneDrive\\Desktop\\BlinkIT_Grocery_Data.csv\")\n",
    "\n",
    "print(\"Initial shape:\", df.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93b5af09-8e6b-4499-875a-b7c4abe93a33",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Standardize column names\n",
    "df.columns = (\n",
    "    df.columns\n",
    "    .str.strip()\n",
    "    .str.lower()\n",
    "    .str.replace(\" \", \"_\")\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c5e36d6-83d4-4923-a900-518d51a0ea5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Handle missing Item Weight\n",
    "if \"item_weight\" in df.columns:\n",
    "    df[\"item_weight\"] = df[\"item_weight\"].fillna(df[\"item_weight\"].median())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c055dfdb-975a-4df6-a386-012ca1350d19",
   "metadata": {},
   "outputs": [],
   "source": [
    "#fix zero / missing Item Visibility\n",
    "if \"item_visibility\" in df.columns:\n",
    "    visibility_median = df[\"item_visibility\"].replace(0, pd.NA).median()\n",
    "    df[\"item_visibility\"] = df[\"item_visibility\"].replace(0, visibility_median)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce2771a5-25c3-4442-8bfd-45fddb4891b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Clean Fat Content values\n",
    "if \"item_fat_content\" in df.columns:\n",
    "    df[\"item_fat_content\"] = df[\"item_fat_content\"].replace({\n",
    "        \"low fat\": \"Low Fat\",\n",
    "        \"LF\": \"Low Fat\",\n",
    "        \"lf\": \"Low Fat\",\n",
    "        \"reg\": \"Regular\",\n",
    "        \"regular\": \"Regular\"\n",
    "    })"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dd3837f-5e3b-4fce-91b5-bf3b32bad3c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create Outlet Age feature\n",
    "if \"outlet_establishment_year\" in df.columns:\n",
    "    CURRENT_YEAR = 2024\n",
    "    df[\"outlet_age\"] = CURRENT_YEAR - df[\"outlet_establishment_year\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "728c5848-d21e-42df-b14b-002b495018a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Basic sanity checks\n",
    "df = df.drop_duplicates()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
