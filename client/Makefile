SERVICE_NAME=log-client
SERVICE_SCRIPT=client.sh
SERVICE_UNIT=log-client.service
INSTALL_DIR=/usr/lib/log-client
SYSTEMD_DIR=/etc/systemd/system
CONF_FILE=conf

.PHONY: all install uninstall clean

all: install

install: $(SERVICE_SCRIPT) $(SERVICE_UNIT)
	#Create dir
	mkdir -p $(INSTALL_DIR) 
	@echo "Installing $(SERVICE_NAME) service..."
	# Copy the service script to the install directory
	install -m 755 $(SERVICE_SCRIPT) $(INSTALL_DIR)/$(SERVICE_SCRIPT)
	# Copy conf file
	install -m 644 $(CONF_FILE) $(INSTALL_DIR)/$(CONF_FILE)
	# Copy the systemd service unit file to the systemd directory
	install -m 644 $(SERVICE_UNIT) $(SYSTEMD_DIR)/$(SERVICE_UNIT)
	# Reload systemd to recognize the new service
	systemctl daemon-reload
	# Enable the service to start on boot
	systemctl enable $(SERVICE_NAME).service
	# Start the service
	systemctl start $(SERVICE_NAME).service
	@echo "$(SERVICE_NAME) service installed and started."

uninstall:
	@echo "Uninstalling $(SERVICE_NAME) service..."
	# Stop the service
	systemctl stop $(SERVICE_NAME).service
	# Disable the service
	systemctl disable $(SERVICE_NAME).service
	# Remove the service script from the install directory
	rm -f $(INSTALL_DIR)/$(SERVICE_SCRIPT)
	# Remove the systemd service unit file
	rm -f $(SYSTEMD_DIR)/$(SERVICE_UNIT)
	# Reload systemd to apply the changes
	systemctl daemon-reload
	@echo "$(SERVICE_NAME) service uninstalled."

clean:
	@echo "Cleaning up..."
	# Add any cleanup commands if necessary
	@echo "Cleanup complete."

