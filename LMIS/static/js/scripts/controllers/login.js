var loginAppModule = angular.module('loginApp').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

loginAppModule.controller('LoginCtrl',  function ($scope) {
$scope.phones = [
{'name': 'Nexus S',
'snippet': 'Fast just got faster with Nexus S.'},
{'name': 'Motorola XOOM™ with Wi-Fi',
'snippet': 'The Next, Next Generation tablet.'},
{'name': 'MOTOROLA XOOM™',
'snippet': 'The Next, Next Generation tablet.'}
];
});


var phonecatApp = angular.module('phonecatApp', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

phonecatApp.controller('PhoneListCtrl', function ($scope) {
    $scope.phones = [
        {'name': 'Nexus S', 'snippet': 'Fast just got faster with Nexus S.'},
        {'name': 'Motorola XOOM™ with Wi-Fi', 'snippet': 'The Next, Next Generation tablet.'},
        {'name': 'MOTOROLA XOOM™', 'snippet': 'The Next, Next Generation tablet.'}
    ];
});