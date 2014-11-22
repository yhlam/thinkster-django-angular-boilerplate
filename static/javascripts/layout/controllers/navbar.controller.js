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

    activate();

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf thinkster.layout.controllers.NavbarController
     */
    function activate() {
      $scope.$watchCollection(function () { return Authentication.getAuthenticatedAccount(); }, updateUser);

      /**
      * @name updateUser
      * @desc Update the username in navbar
      * @param {User} current The current authenticated account
      * @param {User} original The authenticated account before it was updated
      * @memberOf thinkster.layout.controllers.NavbarController
      */
      function updateUser(current, original) {
        if(current != original) {
          vm.user = current;
        }
      }
    }
  }
})();
