vagrand up
vagrand ssh

sudo docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password

http://192.168.56.10:80/users/sign_in

root
<password>

В web-интерфейсе GitLab:
Admin Area → CI/CD → Runners → Registration token

Заменяем в vars.yml знаечние токена

Запускаем setup-runners playbook:

ssh-keygen -f ~/.ssh/known_hosts -R 192.168.56.10
ansible-playbook -i ansible/host-debug ansible/setup-runner.yml


git clone http://192.168.56.10/root/api_service.git
cd api_service/
git add .
git config user.name "root"
git config user.email "root@example.com"
git commit -m "Commit with vulnerability"
git push origin main



sudo docker run -d   --name gitlab-runner   --restart always   --privileged   -v /srv/gitlab-runner/config:/etc/gitlab-runner   -v /var/run/docker.sock:/var/run/docker.sock   gitlab/gitlab-runner:latest