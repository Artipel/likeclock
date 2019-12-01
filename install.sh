set -e
LOC=`pwd`
echo "Creating start script..."
echo "/usr/bin/python3 ${LOC}/main_routine.py" > clock.sh
echo "Done!"
echo "Adding executable permission to script..."
chmod +x "${LOC}/clock.sh"
echo "Done!"
echo "Adjusting service unit..."
sed -i "s|%%LOC%%|${LOC}/clock.sh|g" likeclock.service
echo "Done!"
echo "Copying application configuration (config.json) to boot directiory if not exists"
sudo cp -n "${LOC}/config.json" "/boot/config.json"
echo "Done"
echo "Copying service unit..."
sudo scp "${LOC}/likeclock.service" /etc/systemd/system/likeclock.service
echo "Done!"
echo "Enabling service unit"
sudo systemctl enable likeclock.service
echo "Done!"
echo "Starting service unit"
sudo systemctl start likeclock.service
echo "Done!"
echo "Install completed"
echo "Service status:"
systemctl status likeclock
echo "Type systemctl status likeclock after some time to check if it works OK"
