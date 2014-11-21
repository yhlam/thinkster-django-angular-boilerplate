/**
 * NavbarController
 * @namespace thinkster.layout.controllers
 */
(function() {
  'use strict';

  angular
    .module('thinkster.layout.controllers')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['$scope', '$window', 'Authentication'];

  /**
   * @namespace NavbarController
   */
  function NavbarController($scope, $window, Authentication) {
    var vm = this;

    vm.user = Authentication.getAuthenticatedAccount();
    vm.logout = logout;


    function logout() {
      Authentication.logout();
      $window.location = '/';
    }
  }
})();
