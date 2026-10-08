import os
import sys
import subprocess
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
APP_DIR = BASE_DIR / "app"

print("=" * 60)
print("⚡  ELECTRICITY CONSUMPTION OPTIMIZER")
print("    AI-Powered Household Energy Management System")
print("=" * 60)


# ============================================================
# STEP 1: Generate Dataset
# ============================================================

print("\n📊 STEP 1: Generating dataset...")

generate_script = DATA_DIR / "generate_data.py"

subprocess.run(
    [sys.executable, str(generate_script)],
    cwd=str(DATA_DIR),
    check=True
)

print("✅ Dataset ready!")


# ============================================================
# STEP 2: Preprocess Data
# ============================================================

print("\n🧹 STEP 2: Preprocessing data...")

from data_preprocessing import (
    load_data,
    clean_data,
    get_daily_data,
    detect_anomalies,
    calculate_bill,
    prepare_ml_data
)

electricity_file = DATA_DIR / "electricity_data.csv"

df = load_data(str(electricity_file))
df = clean_data(df)

daily_df = get_daily_data(df)

daily_df, anomalies = detect_anomalies(daily_df)

daily_df["bill"] = daily_df["usage_kwh"].apply(calculate_bill)

daily_clean_file = DATA_DIR / "daily_clean.csv"
daily_df.to_csv(daily_clean_file, index=False)

print("✅ Preprocessing complete!")


# ============================================================
# STEP 3: Train LSTM Model
# ============================================================

print("\n🤖 STEP 3: Training LSTM model...")
print("   (This may take 2-5 minutes...)")

from train_model import (
    build_model,
    train_model,
    evaluate_model
)

X_train, X_test, y_train, y_test, scaler = prepare_ml_data(daily_df)

model = build_model(sequence_length=30)

model, history = train_model(
    model,
    X_train,
    y_train
)

y_pred, y_test_actual = evaluate_model(
    model,
    X_test,
    y_test,
    scaler
)

print("✅ Model trained and saved!")


# ============================================================
# STEP 4: Launch Dashboard
# ============================================================

print("\n🚀 STEP 4: Launching dashboard...")
print("   Opening http://localhost:8501")
print("   Press Ctrl+C to stop the dashboard")
print("=" * 60)

dashboard_file = APP_DIR / "dashboard.py"

subprocess.run(
    [sys.executable, "-m", "streamlit", "run", str(dashboard_file)],
    cwd=str(BASE_DIR)
)