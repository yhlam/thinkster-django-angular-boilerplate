/**
 * NavbarController
 * @namespace thinkster.layout.controllers
 */
(function() {
  'use strict';

  angular
    .module('thinkster.layout.controllers')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['$scope', 'Authentication'];

  /**
   * @namespace NavbarController
   */
  function NavbarController($scope, Authentication) {
    var vm = this;

    vm.user = Authentication.getAuthenticatedAccount();
  }
})();
