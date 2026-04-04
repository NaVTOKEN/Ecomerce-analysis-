def run_checks(df):
    errors = []

    if df.isnull().sum().sum() > 0:
        errors.append("Null values found")

    if df.duplicated().sum() > 0:
        errors.append("Duplicate records found")

    if (df["quantity"] < 0).any():
        errors.append("Negative quantity found")

    if (df["price"] < 0).any():
        errors.append("Negative price found")

    if errors:
        raise Exception(f"Data Quality Failed: {errors}")

    print("✅ Data Quality Passed")
