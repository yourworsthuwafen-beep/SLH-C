.PHONY: install uninstall

install:
	@echo "Creating installation directory..."
	sudo mkdir -p /opt/super-slaughter-house
	@echo "Copying game files and assets..."
	sudo cp -r . /opt/super-slaughter-house
	@echo "Fixing file permissions..."
	sudo chown -R $$USER:$$USER /opt/super-slaughter-house
	sudo chmod +x /opt/super-slaughter-house/Slaughterhouse.bin
	@echo "Creating global terminal shortcut 'slh'..."
	echo '#!/bin/sh' | sudo tee /usr/local/bin/slh > /dev/null
	echo 'cd /opt/super-slaughter-house && ./Slaughterhouse.bin "$$@"' | sudo tee -a /usr/local/bin/slh > /dev/null
	sudo chmod +x /usr/local/bin/slh
	@echo "Done! Run 'slh' from any terminal."

uninstall:
	@echo "Removing installation directory..."
	sudo rm -rf /opt/super-slaughter-house
	@echo "Removing terminal shortcuts..."
	sudo rm -f /usr/local/bin/slh
	sudo rm -f /usr/local/bin/super-slaughter-house
	@echo "Uninstallation complete."
