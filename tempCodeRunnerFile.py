def process_message(msg):
    data = json.loads(msg.value().decode('utf-8'))
    # Perform data processing here (e.g., transform, aggregate, filter)
    processed_data = {
        "user_id": data["user_id"],
        "device_type": data["device_type"],
        "locale": data["locale"],
        "processed_at": data["timestamp"]
    }
    return json.dumps(processed_data).encode('utf-8')