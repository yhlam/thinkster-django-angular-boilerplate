/**
 * ProfileSettingsController
 * @namespace thinkster.porfile.contollers
 */
(function() {
  'use strict';

  angular
    .module('thinkster.profile.controllers')
    .controller('ProfileSettingsController', ProfileSettingsController);

  ProfileSettingsController.$inject = [
    '$location', '$routeParams', 'Authentication', 'Profile', 'Snackbar'
  ]

  /**
   * @namespace ProfileSettingsController
   */
  function ProfileSettingsController($location, $routeParams, Authentication, Profile, Snackbar) {
    var vm = this;

    vm.destroy = destroy;
    vm.update = update;

    activate();


    /**
     * @name active
     * @desc Actions to be performed when this controller is instantiated.
     * @memberOf thinkster.profile.contollers.ProfileSettingsController
     */
    function activate() {
      var authenticatedAccount = Authentication.getAuthenticatedAccount();
      var username = $routeParams.username.substr(1);

      if(!authenticatedAccount || authenticatedAccount.username !== username) {
        // Redirect if not logged in or not the owner of this profile.
        $location.url('/');
        Snackbar.error('You are not authorized to view this page.');
      }

      Profile.get(username).then(profileSuccessFn, profileErrorFn);

      /**
       * @name profileSuccessFn
       * @desc Update `profile` for view
       */
      function profileSuccessFn(data, status, headers, config) {
        vm.profile = data.data;
      }

      /**
       * @name profileErrorFn
       * @desc Redirect to index
       */
      function profileErrorFn(data, status, headers, config) {
        $location.url('/');
        Snackbar.error('That user does not exist.');
      }
    }

    /**
     * @name destroy
     * @desc Destroy this user's profile
     * @memberOf thinkster.profile.contollers.ProfileSettingsController
     */
    function destroy() {
      Profile.destroy(vm.profile).then(profileSuccessFn, profileErrorFn);

      /**
       * @name profileSuccessFn
       * @desc Redirect to index and display success snackbar
       */
      function profileSuccessFn(data, status, headers, config) {
        Authentication.logout();
        $location.url('/');

        Snackbar.show('Your account has been deleted.');
      }

      /**
       * @name profileErrorFn
       * @desc Display error snackbar
       */
      function profileErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }

    /**
     * @name update
     * @desc Update this user's profile
     * @memberOf thinkster.profile.contollers.ProfileSettingsController
     */
    function update() {
      Profile.update(vm.profile).then(profileSuccessFn, profileErrorFn);

      /**
       * @name profileSuccessFn
       * @desc Suhow success snackbar
       */
      function profileSuccessFn(data, status, headers, config) {
        Snackbar.show('Your account has been updated.');
      }

      /**
       * @name profileErrorFn
       * @desc Display error snackbar
       */
      function profileErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }
  }
})();
