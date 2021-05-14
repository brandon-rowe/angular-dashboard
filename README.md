# angular-dashboard
Angular,  NodeJS, Nginx, MongoDB

by [brandon-rowe](https://github.com/brandon-rowe) , [dylan-napoli](https://github.com/dnapoli97) , and {Kailyn](https://github.com/kailynw)

[![license](https://img.shields.io/github/license/tomastrajan/angular-ngrx-material-starter.svg)](https://github.com/brandon-rowe/angular-dashboard/blob/master/LICENSE) [![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors) [![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier) [![Build Status](https://travis-ci.org/tomastrajan/angular-ngrx-material-starter.svg?branch=master)](https://travis-ci.org/tomastrajan/angular-ngrx-material-starter) 

## References

### Angular
+ [Angular](https://angular.io)
+ [Angular Documentation](https://angular.io/docs)

### NodeJS
+ [Configure NodeJS on Server](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-node-js-application-for-production-on-ubuntu-18-04)

### MongoDB

### UPDATE: server_config.sh sets up server and takes care of Items 2 - 4 Manage Server & Config Nginx

### Digitalocean and Nginx
+ [Configure Digitalocean Server Droplet](https://www.digitalocean.com/docs/droplets/how-to/create/)
+ [Manage Ubuntu Server Droplet](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04)
+ [Install and Config Nginx on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04)
+ [Configure Server Blocks with Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
+ [Configure Nginx to run PHP](https://websiteforstudents.com/setup-nginx-web-servers-with-php-support-on-ubuntu-servers/)
+ [Configure SSL with CertBot Nginx](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04)
+ [Configure Uncomplicated Firewall](https://www.vultr.com/docs/how-to-configure-ufw-firewall-on-ubuntu-14-04)

## Configure Server
```bash
git clone https://github.com/brandon-rowe/angular-dashboard
cd angular-dashboard
bash server_config.sh
```

## Getting started (Install)
```bash
npm install -g @angular/cli
bash ng serinstall.bash
```

## Running Frontend (Angular)
```
ng serve
```
## Running Backend (Node)
```bash
cd server/
npm start
```


---
## Other
### Useful Commands
  * `ng serve` - starts a dev server and opens browser with running app
  * `ng build --prod` - build dist folder for web deployment of app
  * `npm start` - starts a dev server and opens browser with running app
  * `npm run test` - runs lint and tests
  * `npm run watch` - runs tests in watch mode
  * `npm run prod` - runs full prod build and serves prod bundle
  * `npm run prettier` - runs prettier to format whole code base (`.ts` and `.scss`) 
  * `npm run analyze` - runs full prod build and `webpack-bundle-analyzer` to visualize how much code is shipped (dependencies & application) 

### Make It Your Own
When using this starter project to build your own app you might consider some of the following steps:
  
  * use `search and replace` functionality of your favourite IDE to replace `anms` with `<your-app-prefix>`
  * rename project in `package.json` `name` property and set appropriate version (eg `0.0.0` or `1.0.0`)
  * rename app in `src/environments/` files (will be shown in browser tab)
  * delete pre-existing `CHANGELOG.md` (you will generate your own with future releases of your features)
  * delete `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` and `BUILT_WITH.md` files as they are relevant only if project is open sourced on Github
  * remove or adjust links in the [footer](https://github.com/tomastrajan/angular-ngrx-material-starter/blob/master/src/app/app.component.html#L79)
  * replace logo in `src/assets` folder ( currently 128 x 128 pixel `png` file )
  * adjust colors in `src/themes/default-theme.scss`
  * create a pull request in the [original repository](https://github.com/tomastrajan/angular-ngrx-material-starter/) to update `BUILT_WITH.md` [file](https://github.com/tomastrajan/angular-ngrx-material-starter/blob/master/BUILT_WITH.md) with a link and short description of your project
  
#### Continuous Integration
Starter project is using [Travis CI](https://travis-ci.org/) for running linters and tests on every commit.
Based on your preferences and needs you can either:

  * not use / use other CI server and delete both `.travis.yml` and `.travis-deploy.sh`
  * create Travis CI account and link it to your projects Github repo and [configure build](https://medium.com/@tomastrajan/continuous-deployment-of-client-side-apps-with-github-pages-travis-ci-10e9d641a889) 
    with `GH_REF` and `GH_TOKEN` environment variables for automatic deployment of releases to Github Pages
  

### Learning Materials
Articles with content that explains various approaches used to build this starter project.

  * [Blog post about Best Practices for Angular CLI](https://medium.com/@tomastrajan/6-best-practices-pro-tips-for-angular-cli-better-developer-experience-7b328bc9db81) used in this starter project
  * [Blog post about Typescript tips for Ngrx reducer code](https://medium.com/@tomastrajan/object-assign-vs-object-spread-in-angular-ngrx-reducers-3d62ecb4a4b0)
  * [Blog post about building responsive layouts with Bootstrap 4 in Angular apps](https://medium.com/@tomastrajan/how-to-build-responsive-layouts-with-bootstrap-4-and-angular-6-cfbb108d797b)
  * [Blog post about configuration of animations during runtime](https://medium.com/tomastrajan/total-guide-to-dynamic-angular-animations-that-can-be-toggled-at-runtime-be5bb6778a0a)
  * [Blog post about unit testing of components with NgRx TestStore](https://medium.com/@tomastrajan/how-to-unit-test-angular-components-with-fake-ngrx-teststore-f0500cc5fc26)
  * [Blog post about Angular CLI budgets](https://medium.com/@tomastrajan/how-did-angular-cli-budgets-save-my-day-and-how-they-can-save-yours-300d534aae7a)
 
### Features

* custom theme support
* lazy-loading of feature modules
* lazy reducers
* localStorage ui state persistence
* `@ngrx/effects` for API requests
* fully responsive design
* angular-material and custom components in `SharedModule`
 
### Stack

* Angular
* HTML, CSS
* JavaScript
* NodeJS
* MongoDB
* Bootstrap 4 (only reset, utils and grids)

### Troubleshooting

* **Blocking at emitting LicenseWebpackPlugin when npm start** - try using [cnpm](https://github.com/cnpm/cnpm) instead of npm
<!--
## Contributors
Want to start contributing to open source? 

Leave your mark and join the growing team of contributors!

Get started by checking out list of open [issues](https://github.com/brandon-rowe/JS/issues) and reading [Contributor Guide](https://github.com/brandon-rowe/JS/CONTRIBUTING.md)
