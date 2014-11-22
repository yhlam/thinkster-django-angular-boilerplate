/**
 * ProfileController
 * @namespace thinkster.profile.controllers
 */
(function() {
  'use strict';

  angular
    .module('thinkster.profile.controllers')
    .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['$location', '$routeParams', 'Post', 'Profile', 'Snackbar'];

  /**
   * @namespace ProfileController
   */
  function ProfileController($location, $routeParams, Post, Profile, Snackbar) {
    var vm = this;

    vm.profile = undefined;
    vm.posts = [];

    activate();

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf thinkster.profile.controllersProfileController
     */
    function activate() {
      var username = $routeParams.username.substr(1);

      Profile.get(username).then(profileSuccessFn, profileErrorFn);
      Post.get(username).then(postSuccessFn, postErrorFn);

      /**
       * @name profileSuccessProfile
       * @desc Update `profile` on viewmodel
       */
      function profileSuccessFn(data, status, headers, config) {
        vm.profile = data.data;
      }

      /**
       * @name profileErrorFn
       * @desc Redirect to index to show error Snackbar
       */
      function profileErrorFn(data, status, headers, config) {
        $location.url('/');
        Snackbar.error('That user does not exist.');
      }

      /**
       * @name postSuccessFn
       * @desc Update `posts` on viewmodel
       */
      function postSuccessFn(data, status, headers, config) {
        vm.posts = data.data;
      }

      /**
       * @name postErrorFn
       * @desc Show error snackbar
       */
      function postErrorFn(data, status, headers, config) {
        Snackbar.error(data.data.error);
      }
    }
  }
})();
