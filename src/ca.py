import os

# Contract address can be provided by the environment (useful for deployment)
# Fallback to the last known local address used during development
powerContractAddress = os.getenv(
	"CONTRACT_ADDRESS",
	"0x537b0b1605dB19d868afd2c298cDF94827Bd1457",
)