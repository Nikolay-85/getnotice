# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provider "virtualbox" do |v|
    v.memory = 512
    v.cpus = 1
  end

  config.vm.box = "debian/jessie64"

  #config.vm.box_url = "https://github.com/holms/vagrant-jessie-box/releases/download/Jessie-v0.1/Debian-jessie-amd64-netboot.box"
  config.vm.box_url = "http://static.gender-api.com/debian-8-jessie-rc2-x64-slim.box"
  config.vm.network "private_network", ip: "192.168.150.150"
  config.vm.synced_folder ".", "/home/vagrant/getnotice"
  config.vm.network "forwarded_port", guest: 8000, host: 8080
  #config.vm.synced_folder ".", "/app"
  #config.vm.share_folder "project", "/home/vagrant/getnotice", "."	
  #config.vm.provision "docker"

  #config.vm.provision "shell",
  #  :path => "config/setup.sh"
  config.vm.provision :shell, :path => "config/setup.sh", :args => "{{ project_name }}"

end
