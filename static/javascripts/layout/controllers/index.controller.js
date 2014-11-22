/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function() {
  'use strict';

  angular
    .module('thinkster.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Authentication', 'Post', 'Snackbar'];

  /**
   * @namespace IndexController
   */
  function IndexController($scope, Authentication, Post, Snackbar) {
    var vm = this;

    vm.isAuthenticated = Authentication.isAuthenticated();
    vm.posts = []

    activate();

    /**
     * @name activate
     * @desc
     * @memberOf thinkster.layout.controllers.IndexController
     */
    function activate() {
      Post.all().then(postSuccessFn, postErrorFn);

      $scope.$on('post.created', function(event, post) {
        vm.posts.unshift(post);
      });

      $scope.$on('post.created.error', function(event, post) {
        vm.posts.shift();
      });


      /**
       * @name postSucessFn
       * @desc Update thoughts array on view
       */
      function postSuccessFn(data, status, headers, config) {
        vm.posts = data.data;
      }


      /**
       * @name postErrorFn
       * @desc Show snackbar with error
       */
      function postErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }
  }
})();
