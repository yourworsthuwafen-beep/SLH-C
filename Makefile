.PHONY: install uninstall

install:
	@echo "Creating installation directory..."
	sudo mkdir -p /opt/super-slaughter-house
	@echo "Copying game files and assets..."
	sudo cp -r . /opt/super-slaughter-house
	@echo "Fixing file permissions..."
	sudo chown -R $$USER:$$USER /opt/super-slaughter-house
	@echo "Creating global terminal shortcut 'slh'..."
	echo '#!/bin/sh' | sudo tee /usr/local/bin/slh > /dev/null
	echo 'cd /opt/super-slaughter-house && python3 Slaughterhouse.py "$$@"' | sudo tee -a /usr/local/bin/slh > /dev/null
	sudo chmod +x /usr/local/bin/slh
	@echo "Done! Run 'slh' from any terminal."

uninstall:
	sudo rm -rf /opt/super-slaughter-house
	sudo rm -f /usr/local/bin/slh
	sudo rm -f /usr/local/bin/super-slaughter-house
