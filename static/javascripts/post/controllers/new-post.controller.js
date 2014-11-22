/**
 * NewPostController
 * @namespace thinkster.post.controllers
 */
(function () {
  'use strict';

  angular
    .module('thinkster.post.controllers')
    .controller('NewPostController', NewPostController);

  NewPostController.$inject = ['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Post'];

  /**
   * @namespace NewPostController
   */
  function NewPostController($rootScope, $scope, Authentication, Snackbar, Post) {
    var vm = this;

    vm.submit = submit;

    /**
     * @name submit
     * @desc Create a new post
     * @memberOf thinkster.post.controllers.NewPostController
     */
    function submit() {
      $rootScope.$broadcast('post.created', {
        content: vm.content,
        author: {
          username: Authentication.getAuthenticatedAccount().username
        }
      });

      $scope.closeThisDialog();

      Post.create(vm.content).then(createPostSuccessFn, createPostErrorFn);


      /**
       * @name createPostSuccessFn
       * @desc Show snackbar with success messge
       */
      function createPostSuccessFn(data, status, headers, config) {
        Snackbar.show('Success! Post created.');
      }


      /**
       * @name createPostErrorFn
       * @desc Propergate error event and show snackbar with error message
       */
      function createPostErrorFn(data, status, headers, config) {
        $rootScope.$broadcast('post.created.error');
        Snackbar.error(data.error);
      }
    }
  }
})();
